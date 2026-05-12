from flask import Flask, render_template, request, redirect, session, jsonify, flash
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os
from functools import wraps
import config

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = app.config['SECRET_KEY']
DB_PATH = app.config['DATABASE']

def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = conectar()
    c = conn.cursor()
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL,
        email TEXT UNIQUE,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        categoria TEXT,
        status TEXT DEFAULT 'vigente',
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    """)
    
    c.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        cor TEXT DEFAULT '#60a5fa',
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    """)
    
    conn.commit()

    c.execute("PRAGMA table_info(transacoes)")
    existing_columns = {row[1] for row in c.fetchall()}
    if 'usuario_id' not in existing_columns:
        c.execute("ALTER TABLE transacoes ADD COLUMN usuario_id INTEGER NOT NULL DEFAULT 1")
    if 'categoria' not in existing_columns:
        c.execute("ALTER TABLE transacoes ADD COLUMN categoria TEXT")
    if 'status' not in existing_columns:
        c.execute("ALTER TABLE transacoes ADD COLUMN status TEXT DEFAULT 'vigente'")
    if 'data_criacao' not in existing_columns:
        c.execute("ALTER TABLE transacoes ADD COLUMN data_criacao TIMESTAMP")
    if 'data_atualizacao' not in existing_columns:
        c.execute("ALTER TABLE transacoes ADD COLUMN data_atualizacao TIMESTAMP")

    if 'data_criacao' not in existing_columns:
        c.execute("UPDATE transacoes SET data_criacao = CURRENT_TIMESTAMP WHERE data_criacao IS NULL")
    if 'data_atualizacao' not in existing_columns:
        c.execute("UPDATE transacoes SET data_atualizacao = CURRENT_TIMESTAMP WHERE data_atualizacao IS NULL")

    conn.commit()
    conn.close()

criar_tabelas()

# Usuário padrão (admin/admin com hash)
def criar_usuario_padrao():
    conn = conectar()
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM usuarios WHERE username = ?", ("admin",))
        if not c.fetchone():
            hash_senha = generate_password_hash("admin", method=config.HASH_METHOD)
            c.execute("""
            INSERT INTO usuarios (username, senha_hash, email) 
            VALUES (?, ?, ?)
            """, ("admin", hash_senha, "admin@example.com"))
            conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()

criar_usuario_padrao()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("usuario_id"):
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        senha = request.form.get("senha", "")
        
        if not username or not senha:
            flash("Usuário e senha são obrigatórios", "error")
            return render_template("login.html")
        
        conn = conectar()
        c = conn.cursor()
        c.execute("SELECT id, senha_hash FROM usuarios WHERE username = ? OR email = ?", (username, username))
        usuario = c.fetchone()
        conn.close()
        
        if usuario and check_password_hash(usuario[1], senha):
            session.permanent = True
            session["usuario_id"] = usuario[0]
            session["username"] = username
            return redirect("/dashboard")
        else:
            flash("Usuário ou senha inválidos", "error")
    
    if session.get("usuario_id"):
        return redirect("/dashboard")
    
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    usuario_id = session.get("usuario_id")
    
    conn = conectar()
    c = conn.cursor()
    
    # Buscar todas as transações do usuário
    c.execute("""
    SELECT * FROM transacoes 
    WHERE usuario_id = ? 
    ORDER BY data_criacao DESC
    """, (usuario_id,))
    dados = c.fetchall()
    
    # Calcular resumo
    receitas = sum(dict(t)["valor"] for t in dados if dict(t)["tipo"] == "receita")
    despesas = sum(dict(t)["valor"] for t in dados if dict(t)["tipo"] == "despesa")
    investimentos = sum(dict(t)["valor"] for t in dados if dict(t)["tipo"] == "investimento")
    dividas_pagas = sum(dict(t)["valor"] for t in dados if dict(t)["tipo"] == "divida" and dict(t)["status"] == "pago")
    dividas_pendentes = sum(dict(t)["valor"] for t in dados if dict(t)["tipo"] == "divida" and dict(t)["status"] == "pendente")
    
    saldo = receitas - despesas - investimentos - dividas_pagas
    
    # Buscar categorias
    c.execute("""
    SELECT DISTINCT categoria FROM transacoes 
    WHERE usuario_id = ? AND categoria IS NOT NULL
    ORDER BY categoria
    """, (usuario_id,))
    categorias = [row[0] for row in c.fetchall()]
    
    conn.close()
    
    return render_template("dashboard.html",
        transacoes=dados,
        receitas=f"{receitas:.2f}",
        despesas=f"{despesas:.2f}",
        investimentos=f"{investimentos:.2f}",
        dividas=f"{dividas_pendentes:.2f}",
        saldo=f"{saldo:.2f}",
        categorias=categorias,
        total_transacoes=len(dados)
    )
  
@app.route("/add", methods=["POST"])
@login_required
def add():
    usuario_id = session.get("usuario_id")
    
    try:
        tipo = request.form.get("tipo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        valor = float(request.form.get("valor", 0))
        categoria = request.form.get("categoria", "").strip() or None
        
        if (
            tipo not in config.ALLOWED_TYPES
            or not descricao
            or len(descricao) > config.DESCRICAO_MAX_LENGTH
            or valor < config.VALOR_MINIMO
        ):
            flash("Dados inválidos", "error")
            return redirect("/dashboard")

        if categoria and len(categoria) > config.CATEGORIA_MAX_LENGTH:
            flash("Categoria muito longa", "error")
            return redirect("/dashboard")

        status = "pendente" if tipo == "divida" else "vigente"

        conn = conectar()
        c = conn.cursor()
        c.execute("""
        INSERT INTO transacoes (usuario_id, tipo, descricao, valor, categoria, status, data_criacao, data_atualizacao)
        VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """, (usuario_id, tipo, descricao, valor, categoria, status))
        conn.commit()
        conn.close()
        
        flash(f"Transação adicionada com sucesso: R$ {valor:.2f}", "success")
    except ValueError:
        flash("Valor deve ser um número", "error")
    except Exception as e:
        flash(f"Erro ao adicionar transação: {str(e)}", "error")
    
    return redirect("/dashboard")

@app.route("/pay/<int:id>")
@login_required
def pay(id):
    usuario_id = session.get("usuario_id")
    
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    UPDATE transacoes 
    SET status = 'pago', data_atualizacao = CURRENT_TIMESTAMP 
    WHERE id = ? AND usuario_id = ? AND tipo = 'divida'
    """, (id, usuario_id))
    conn.commit()
    conn.close()
    
    flash("Dívida marcada como paga", "success")
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
@login_required
def delete(id):
    usuario_id = session.get("usuario_id")
    
    conn = conectar()
    c = conn.cursor()
    c.execute("""
    DELETE FROM transacoes 
    WHERE id = ? AND usuario_id = ?
    """, (id, usuario_id))
    conn.commit()
    conn.close()
    
    flash("Transação deletada com sucesso", "success")
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta", "info")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])

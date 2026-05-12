"""
Testes básicos para Finance Pro
Execute com: python -m pytest test_app.py
"""

import pytest
import sys
sys.path.insert(0, '.')

def test_imports():
    """Testa se todos os imports funcionam"""
    try:
        from app import app, conectar, criar_tabelas, criar_usuario_padrao
        assert app is not None
        print("✓ Imports OK")
    except Exception as e:
        print(f"✗ Import failed: {e}")
        raise

def test_database_creation():
    """Testa se o banco de dados é criado"""
    import os
    from app import criar_tabelas, DB_PATH
    
    # Remove BD anterior se existir
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    
    criar_tabelas()
    assert os.path.exists(DB_PATH), "Banco de dados não foi criado"
    print("✓ Database creation OK")

def test_usuario_padrao():
    """Testa se o usuário padrão é criado"""
    from app import criar_usuario_padrao, conectar
    
    criar_usuario_padrao()
    
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE username = ?", ("admin",))
    user = c.fetchone()
    conn.close()
    
    assert user is not None, "Usuário admin não foi criado"
    print("✓ Default user creation OK")

def test_password_hashing():
    """Testa hash de senha"""
    from werkzeug.security import generate_password_hash, check_password_hash
    
    password = "test123"
    hashed = generate_password_hash(password)
    
    assert check_password_hash(hashed, password), "Hash de senha falhou"
    assert not check_password_hash(hashed, "wrong"), "Validação de hash falhou"
    print("✓ Password hashing OK")

if __name__ == "__main__":
    print("\n🧪 Iniciando testes Finance Pro...\n")
    
    try:
        test_imports()
        test_database_creation()
        test_usuario_padrao()
        test_password_hashing()
        
        print("\n✅ Todos os testes passaram!")
    except Exception as e:
        print(f"\n❌ Teste falhou: {e}")
        sys.exit(1)

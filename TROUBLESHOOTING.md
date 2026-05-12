# 🆘 TROUBLESHOOTING - Finance Pro

## Problemas Comuns e Soluções

### 1. "ModuleNotFoundError: No module named 'flask'"
**Problema:** Flask não está instalado
**Solução:**
```bash
pip install -r requirements.txt
# ou
pip install Flask==2.3.3 Werkzeug==2.3.7
```

### 2. "Port 5000 is already in use"
**Problema:** Porta 5000 já está em uso
**Solução:**
```bash
# Mudar a porta em app.py
app.run(debug=False, host="0.0.0.0", port=5001)

# ou matar o processo:
# Windows: netstat -ano | findstr :5000
# Linux/Mac: lsof -i :5000 | kill PID
```

### 3. "werkzeug.exceptions.NotFound: The requested URL /dashboard was not found"
**Problema:** Não fez login antes de acessar dashboard
**Solução:**
1. Acesse http://localhost:5000
2. Faça login com admin/admin
3. Clique em "Dashboard"

### 4. "Login não funciona, sempre diz que credenciais são inválidas"
**Problema:** Usuário não foi criado corretamente
**Solução:**
```bash
# Delete o banco de dados:
rm financas.db  # ou delete financas.db no Windows

# Reinicie a aplicação - será recriada
python app.py
```

### 5. "Erro: Unable to locate credentials"
**Problema:** Variáveis de ambiente não estão configuradas
**Solução:**
```bash
# Copie o arquivo .env.example
cp .env.example .env

# Configure os valores em .env (opcional)
# A app usará valores padrão se não configurado
```

### 6. "CSS não está sendo carregado"
**Problema:** Arquivo CSS não foi encontrado
**Verificação:**
1. Verifique se `static/style.css` existe
2. Limpe o cache do navegador (Ctrl+Shift+Delete)
3. Verifique a URL no console do navegador (F12)

### 7. "Gráfico não aparece"
**Problema:** Chart.js não carregou ou dados inválidos
**Solução:**
1. Verifique no console (F12) há erros
2. Adicione uma transação primeiro
3. Recarregue a página
4. Verifique internet (CDN precisa estar acessível)

### 8. "Banco de dados não foi criado"
**Problema:** Permissões insuficientes ou erro durante criação
**Solução:**
```bash
# Delete e recrie:
rm financas.db
python app.py
```

### 9. "Transações desaparecem after logout"
**Problema:** Não é problema - são específicas do usuário
**Verificação:**
- Cada usuário vê apenas suas transações
- Logout não deleta dados
- Dados persistem no BD

### 10. "Formulário não envia transação"
**Problema:** Validação falhou
**Verificação:**
1. Todos os campos estão preenchidos?
2. Valor é maior que 0?
3. Tipo de transação está selecionado?
4. Descrição tem mais de 255 caracteres?

---

## Verificações de Diagnóstico

### 1. Verificar Estrutura
```bash
python verify.py
```

### 2. Executar Testes
```bash
python test_app.py
```

### 3. Ver Logs
```bash
# Ativar debug completo
# Editar app.py e setar DEBUG=True
python app.py
```

### 4. Verificar Banco de Dados
```bash
# Inspect SQLite DB
sqlite3 financas.db
sqlite> .tables
sqlite> SELECT * FROM usuarios;
sqlite> SELECT * FROM transacoes;
```

---

## Erros de Sintaxe

### "SyntaxError: invalid syntax"
**Solução:**
```bash
python -m py_compile app.py
```

### "IndentationError: unexpected indent"
**Solução:** Verificar espaçamento em Python (use 4 espaços, não tabs)

---

## Problemas de Performance

### App está lento
**Verifique:**
1. Quantas transações há no BD? `SELECT COUNT(*) FROM transacoes;`
2. Há índices? Adicione: `CREATE INDEX idx_usuario ON transacoes(usuario_id);`
3. Use limite em queries grandes

### Gráfico demora para carregar
**Solução:**
1. Limite transações na tela (adicione paginação)
2. Melhore a query do banco de dados
3. Adicione cache em desenvolvimento

---

## Problemas de Segurança

### "Você pode injetar SQL?"
**Resposta:** Não - estamos usando prepared statements (`?` placeholders)

### "Sessão expirou?"
**Solução:** Configure em config.py:
```python
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
```

---

## Problemas em Produção

### App não inicia no Heroku
```bash
# Check Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
git push heroku main
```

### Banco de dados em produção
- Não use SQLite (use PostgreSQL/MySQL)
- Configure variável DB_URL
- Use alembic para migrações

### HTTPS forçado
```python
app.config['SESSION_COOKIE_SECURE'] = True
```

---

## Suporte

Se o problema persiste:
1. ✅ Verifique esta lista
2. ✅ Rode `verify.py`
3. ✅ Rode `test_app.py`
4. ✅ Verifique logs (console)
5. 💬 Consulte README.md ou DEVELOPMENT.md

---

## Checklist de Debug

- [ ] Python 3.7+ instalado? `python --version`
- [ ] Dependências instaladas? `pip list | grep Flask`
- [ ] Arquivo BD existe ou foi criado?
- [ ] Porta 5000 está disponível?
- [ ] Variáveis de ambiente configuradas?
- [ ] URLs estão corretas?
- [ ] JavaScript console tem erros? (F12)
- [ ] Network tab mostra 200 OK? (F12)
- [ ] Cache limpo? (Ctrl+Shift+Delete)
- [ ] Usando localhost ou 127.0.0.1?

---

**Última atualização:** Abril de 2026
**Versão:** 2.0.0 Pro

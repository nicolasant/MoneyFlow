# Guia de Desenvolvimento - Finance Pro

## 🎯 Arquitetura

### Camadas da Aplicação

1. **Camada de Apresentação (Frontend)**
   - Templates HTML/Jinja2
   - CSS com variáveis de tema
   - JavaScript para interatividade

2. **Camada de Aplicação (Backend)**
   - Flask routes
   - Validação de dados
   - Lógica de negócio

3. **Camada de Dados**
   - SQLite database
   - Operações CRUD

## 🔧 Variáveis de Requisição

### Transações
```python
{
    'id': int,
    'usuario_id': int,
    'tipo': str,  # 'receita', 'despesa', 'investimento', 'divida'
    'descricao': str,
    'valor': float,
    'categoria': str (opcional),
    'status': str,  # 'vigente', 'pago'
    'data_criacao': datetime,
    'data_atualizacao': datetime
}
```

## 📚 Endpoints da Aplicação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET/POST | `/` | Login |
| GET | `/dashboard` | Dashboard principal |
| POST | `/add` | Adicionar transação |
| GET | `/pay/<id>` | Marcar dívida como paga |
| GET | `/delete/<id>` | Deletar transação |
| GET | `/logout` | Logout |

## 🎨 Variáveis CSS Disponíveis

```css
--text: #f1f5f9          /* Texto principal */
--text-secondary: #cbd5e1  /* Texto secundário */
--muted: #94a3b8         /* Texto mutado */
--accent: #60a5fa        /* Cor de destaque */
--success: #22c55e       /* Sucesso (verde) */
--danger: #ef4444        /* Erro (vermelho) */
--warning: #f59e0b       /* Aviso (laranja) */
--info: #06b6d4          /* Info (ciano) */
```

## 🧪 Testes Recomendados

### Testes Manual
- [ ] Login com credenciais válidas
- [ ] Login com credenciais inválidas
- [ ] Adicionar transação de cada tipo
- [ ] Visualizar transações no histórico
- [ ] Marcar dívida como paga
- [ ] Deletar transação
- [ ] Fazer logout
- [ ] Testar responsividade em mobile
- [ ] Verificar gráficos dinamicamente

### Testes de Segurança
- [ ] SQL Injection na entrada
- [ ] XSS no histórico
- [ ] CSRF em mudanças de dados
- [ ] Session hijacking
- [ ] Força bruta em login

## 📦 Deploy

### Produção (Heroku/PythonAnywhere)
```bash
# 1. Defina SECRET_KEY
export SECRET_KEY="sua-chave-segura"

# 2. Defina debug como False
export DEBUG=False

# 3. Configure banco de dados persistente

# 4. Use Gunicorn
pip install gunicorn
gunicorn app:app
```

### Docker (Opcional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```

## 🐛 Debugging

### Modo Debug
O app já inicia em modo debug por padrão. Para desabilitar:
```python
app.run(debug=False)
```

### Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Mensagem de debug")
```

## 📖 Recursos de Aprendizado

- [Flask Documentation](https://flask.palletsprojects.com)
- [SQLite Tutorial](https://www.sqlite.org/index.html)
- [Chart.js Guide](https://www.chartjs.org/docs/latest/)
- [CSS Variables](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

## 🤝 Contribuindo

Para adicionar melhorias:
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

**Última atualização**: Abril de 2026

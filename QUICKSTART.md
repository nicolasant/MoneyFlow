🚀 COMECE AGORA - Finance Pro v2.0.0
=====================================

⚡ OPÇÃO 1: Início Rápido (Recomendado)
────────────────────────────────────

1. Abra o terminal no diretório do projeto

2. Instale dependências:
   $ pip install -r requirements.txt

3. Execute a aplicação:
   $ python app.py

4. Abra no navegador:
   http://localhost:5000

5. Faça login:
   Usuário: admin
   Senha: admin

6. Comece a usar! 🎉


⚙️ OPÇÃO 2: Com Ambiente Virtual (Melhor Prática)
──────────────────────────────────────────────────

1. Crie ambiente virtual:
   
   Windows:
   $ python -m venv venv
   $ venv\Scripts\activate
   
   Mac/Linux:
   $ python3 -m venv venv
   $ source venv/bin/activate

2. Instale dependências:
   $ pip install -r requirements.txt

3. Execute:
   $ python app.py

4. Acesse:
   http://localhost:5000


📝 OPÇÃO 3: Usando o Script de Instalação
──────────────────────────────────────────

Mac/Linux:
$ bash install.sh

Windows (PowerShell):
$ powershell -ExecutionPolicy Bypass -File install.sh


✅ VERIFICAÇÃO RÁPIDA
─────────────────────

Verificar se tudo está instalado:
$ python verify.py

Rodas testes:
$ python test_app.py


🔥 PRIMEIROS PASSOS NA APLICAÇÃO
─────────────────────────────────

1. LOGIN:
   └─ Usuário: admin
   └─ Senha: admin

2. ADICIONAR TRANSAÇÃO:
   └─ Clique no formulário à direita
   └─ Selecione o tipo (Receita, Despesa, etc)
   └─ Preencha descrição e valor
   └─ Clique "Adicionar"

3. VISUALIZAR HISTÓRICO:
   └─ Veja na seção "Histórico"
   └─ Clique no ícone 🗑️ para deletar
   └─ Para dívidas, clique "✓ Pagar"

4. ANALISAR DADOS:
   └─ Veja o gráfico de distribuição
   └─ Observe o saldo total
   └─ Acompanhe receitas e despesas


📚 DOCUMENTAÇÃO
───────────────

Tópico                          Arquivo
─────────────────────────────   ────────────────────
Informações Gerais              README.md
Desenvolvimento/Contribuição    DEVELOPMENT.md
Histórico de Mudanças           CHANGELOG.md
Resumo de Upgrades              UPGRADE_SUMMARY.md
Solução de Problemas            TROUBLESHOOTING.md
Este guia                        QUICKSTART.md


⚠️ CONFIGURAÇÕES IMPORTANTES
──────────────────────────────

Em produção, alterar em config.py:

1. SECRET_KEY (segurança):
   SECRET_KEY = 'sua-chave-segura-aqui'

2. DEBUG (desabilitar debug):
   DEBUG = False

3. HOST (ouvir em interface pública):
   HOST = '0.0.0.0'

4. Usar banco de dados persistente (não SQLite)


🆘 PROBLEMAS?
──────────────

1. Verifique TROUBLESHOOTING.md
2. Execute: python verify.py
3. Execute: python test_app.py
4. Verifique console do navegador (F12)


💡 DICAS
────────

✓ Limpe cache do navegador para mudanças de CSS
✓ Use Ctrl+Click para abrir links em nova aba
✓ Dados são salvos automaticamente
✓ Logout não deleta dados
✓ Cada usuário vê apenas suas transações


🎯 PRÓXIMOS PASSOS
──────────────────

Após explorar a interface:

1. Leia README.md para entender todas funcionalidades
2. Explore DEVELOPMENT.md para contribuir
3. Customize conforme necessário
4. Implante em servidor (Heroku, VPS, etc)


📞 SUPORTE
──────────

Dúvidas?
• Consulte README.md
• Verifique TROUBLESHOOTING.md
• Rode verify.py para diagnóstico


🎉 BEM-VINDO AO FINANCE PRO!

Desenvolvido com ❤️ para melhorar seu controle financeiro

═══════════════════════════════════════════════════════════

Versão: 2.0.0 Pro
Data: 14 de Abril de 2026
Status: ✅ Production Ready

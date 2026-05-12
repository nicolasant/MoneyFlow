"""
Arquivo de configuração da aplicação Finance Pro
"""

import os
from datetime import timedelta

# Ambiente
ENVIRONMENT = os.environ.get('FLASK_ENV', 'development')
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true' or ENVIRONMENT == 'development'

# Segurança
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Sessão
PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Banco de Dados
DATABASE = os.environ.get('DATABASE', 'financas.db')

# Servidor
HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
PORT = int(os.environ.get('FLASK_PORT', 5000))

# Limites
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Validação
ALLOWED_TYPES = ['receita', 'despesa', 'investimento', 'divida']
ALLOWED_STATUS = ['vigente', 'pendente', 'pago']

# Segurança - Hash
HASH_METHOD = 'pbkdf2:sha256'

# Formatação de Valores
CURRENCY_FORMAT = 'pt-BR'
VALOR_MINIMO = 0.01
DESCRICAO_MAX_LENGTH = 255
CATEGORIA_MAX_LENGTH = 50

#!/bin/bash
# Script de instalação rápida para Finance Pro
# Execute: bash install.sh (Linux/Mac) ou execute no PowerShell (Windows)

echo "🚀 Finance Pro - Instalação Rápida"
echo "=================================="
echo ""

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}1. Criando ambiente virtual...${NC}"
python -m venv venv

echo -e "${YELLOW}2. Ativando ambiente virtual...${NC}"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

echo -e "${YELLOW}3. Instalando dependências...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${YELLOW}4. Criando banco de dados...${NC}"
python -c "from app import criar_tabelas, criar_usuario_padrao; criar_tabelas(); criar_usuario_padrao()"

echo ""
echo -e "${GREEN}✅ Instalação concluída com sucesso!${NC}"
echo ""
echo "🎯 Próximos passos:"
echo "1. Execute: python app.py"
echo "2. Acesse: http://localhost:5000"
echo "3. Login: admin / admin"
echo ""
echo "📖 Para mais informações, leia README.md"
echo ""

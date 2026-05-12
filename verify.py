#!/usr/bin/env python
"""
Verificação Final do Finance Pro
Execute: python verify.py
"""

import os
import sys

def check_file(path, name):
    """Verifica se um arquivo existe"""
    exists = os.path.exists(path)
    status = "✅" if exists else "❌"
    print(f"{status} {name}")
    return exists

def check_directory(path, name):
    """Verifica se um diretório existe"""
    exists = os.path.isdir(path)
    status = "✅" if exists else "❌"
    print(f"{status} {name}")
    return exists

def main():
    print("\n" + "="*50)
    print("🔍 VERIFICAÇÃO FINAL - Finance Pro v2.0.0")
    print("="*50 + "\n")
    
    all_ok = True
    
    print("📁 ESTRUTURA DE ARQUIVOS:")
    print("-" * 50)
    
    # Arquivos Python
    print("\n🐍 Arquivos Python:")
    all_ok &= check_file("app.py", "app.py (aplicação principal)")
    all_ok &= check_file("config.py", "config.py (configurações)")
    all_ok &= check_file("test_app.py", "test_app.py (testes)")
    
    # Diretórios
    print("\n📂 Diretórios:")
    all_ok &= check_directory("static", "static/ (arquivos estáticos)")
    all_ok &= check_directory("templates", "templates/ (templates HTML)")
    
    # Arquivos Estáticos
    print("\n🎨 Arquivos Estáticos:")
    all_ok &= check_file("static/style.css", "style.css (estilos)")
    
    # Templates
    print("\n📄 Templates HTML:")
    all_ok &= check_file("templates/base.html", "base.html (template base)")
    all_ok &= check_file("templates/login.html", "login.html (página de login)")
    all_ok &= check_file("templates/dashboard.html", "dashboard.html (dashboard)")
    
    # Configuração
    print("\n⚙️ Arquivos de Configuração:")
    all_ok &= check_file("requirements.txt", "requirements.txt (dependências)")
    all_ok &= check_file(".env.example", ".env.example (variáveis de ambiente)")
    
    # Documentação
    print("\n📚 Documentação:")
    all_ok &= check_file("README.md", "README.md (documentação principal)")
    all_ok &= check_file("DEVELOPMENT.md", "DEVELOPMENT.md (guia de desenvolvimento)")
    all_ok &= check_file("CHANGELOG.md", "CHANGELOG.md (histórico de mudanças)")
    all_ok &= check_file("UPGRADE_SUMMARY.md", "UPGRADE_SUMMARY.md (resumo de upgrades)")
    
    # Scripts
    print("\n🚀 Scripts:")
    all_ok &= check_file("install.sh", "install.sh (script de instalação)")
    
    # Verificar banco de dados
    print("\n💾 Banco de Dados:")
    db_exists = os.path.exists("financas.db")
    status = "✅" if db_exists else "⚠️  (será criado na primeira execução)"
    print(f"{status} financas.db")
    
    print("\n" + "="*50)
    print("📊 VERIFICAÇÃO DE CÓDIGO:")
    print("-" * 50)
    
    try:
        print("\n🔧 Verificando imports...")
        from app import app, conectar, criar_tabelas
        from werkzeug.security import generate_password_hash, check_password_hash
        print("✅ Todos os imports OK")
        
        print("\n✓ Imports validados com sucesso")
        
    except Exception as e:
        print(f"❌ Erro ao importar: {e}")
        all_ok = False
    
    print("\n" + "="*50)
    if all_ok:
        print("✅ VERIFICAÇÃO CONCLUÍDA COM SUCESSO!")
        print("\n🎯 Próximos passos:")
        print("1. Execute: python app.py")
        print("2. Abra: http://localhost:5000")
        print("3. Login: admin / admin")
        print("\n📖 Para mais info, leia README.md")
    else:
        print("⚠️  ALGUNS ARQUIVOS ESTÃO FALTANDO!")
        print("\nReexecute a instalação ou verifique os files.")
    
    print("="*50 + "\n")
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())

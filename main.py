"""
Ponto de entrada principal do Jogo do Leãozinho.
Execute este arquivo para iniciar o jogo com interface gráfica.
"""

import sys
import os

# Adicionar o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar e executar a aplicação GUI
from frontend.main_gui import main

if __name__ == "__main__":
    print("\n🦁 Iniciando Jogo do Leãozinho...")
    print("🎰 Carregando interface gráfica...\n")
    main()

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from frontend.main_gui import main

if __name__ == "__main__":
    print("\n🦁 Iniciando Jogo do Leãozinho...")
    print("🎰 Carregando interface gráfica...\n")
    main()

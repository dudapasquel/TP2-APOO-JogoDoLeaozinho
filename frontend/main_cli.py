"""
Módulo principal do Jogo do Leãozinho.
Implementa a interface de usuário e fluxo do jogo.
"""
import os
import sys
from autenticacao import SistemaAutenticacao
from maquina import Maquina
from usuario import Usuario


class JogoDoLeaozinho:
    """
    Classe principal que gerencia o fluxo do jogo.
    """
    
    def __init__(self):
        """Inicializa o jogo."""
        self._sistema_auth = SistemaAutenticacao()
        self._maquina = Maquina()
        self._usuario_atual = None
    
    def limpar_tela(self):
        """Limpa a tela do console."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_logo(self):
        """Exibe o logo do jogo."""
        print("\n" + "="*60)
        print("""
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║        🦁  JOGO DO LEÃOZINHO - CAÇA-NÍQUEL  🦁        ║
    ║                                                       ║
    ║              💰  Teste sua sorte! 💰                  ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
        """)
        print("="*60 + "\n")
    
    def menu_inicial(self):
        """Exibe o menu inicial e retorna a opção escolhida."""
        print("\n┌─────────────────────────────────────┐")
        print("│         MENU PRINCIPAL              │")
        print("├─────────────────────────────────────┤")
        print("│  1. 🔐 Login                        │")
        print("│  2. 📝 Cadastrar novo usuário       │")
        print("│  3. ❌ Sair                         │")
        print("└─────────────────────────────────────┘")
        
        opcao = input("\nEscolha uma opção: ").strip()
        return opcao
    
    def menu_jogo(self):
        """Exibe o menu do jogo e retorna a opção escolhida."""
        print(f"\n{'='*60}")
        print(f"👤 Usuário: {self._usuario_atual.nome}")
        print(f"💰 Saldo: R$ {self._usuario_atual.get_saldo():.2f}")
        print(f"{'='*60}")
        
        print("\n┌─────────────────────────────────────┐")
        print("│         MENU DO JOGO                │")
        print("├─────────────────────────────────────┤")
        print("│  1. 🎰 Jogar                        │")
        print("│  2. 💵 Depositar créditos           │")
        print("│  3. 📊 Ver tabela de prêmios        │")
        print("│  4. 🚪 Sair e salvar                │")
        print("└─────────────────────────────────────┘")
        
        opcao = input("\nEscolha uma opção: ").strip()
        return opcao
    
    def tela_cadastro(self):
        """Gerencia a tela de cadastro."""
        self.limpar_tela()
        self.exibir_logo()
        
        print("\n📝 CADASTRO DE NOVO USUÁRIO")
        print("-" * 40)
        
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()
        confirma_senha = input("Confirme sua senha: ").strip()
        
        if senha != confirma_senha:
            print("\n❌ Erro: As senhas não coincidem!")
            input("\nPressione ENTER para continuar...")
            return
        
        if self._sistema_auth.cadastrar(nome, senha):
            print("\n✅ Cadastro realizado com sucesso!")
            print("Agora você pode fazer login.")
        
        input("\nPressione ENTER para continuar...")
    
    def tela_login(self):
        """Gerencia a tela de login."""
        self.limpar_tela()
        self.exibir_logo()
        
        print("\n🔐 LOGIN")
        print("-" * 40)
        
        nome = input("Nome de usuário: ").strip()
        senha = input("Senha: ").strip()
        
        usuario = self._sistema_auth.login(nome, senha)
        
        if usuario:
            self._usuario_atual = usuario
            self._maquina.definir_usuario(usuario)
            input("\nPressione ENTER para continuar...")
            self.tela_jogo()
        else:
            input("\nPressione ENTER para continuar...")
    
    def tela_jogo(self):
        """Gerencia a tela principal do jogo."""
        while True:
            self.limpar_tela()
            self.exibir_logo()
            
            opcao = self.menu_jogo()
            
            if opcao == "1":
                self.tela_jogar()
            elif opcao == "2":
                self.tela_deposito()
            elif opcao == "3":
                self.tela_tabela_premios()
            elif opcao == "4":
                self.sair_e_salvar()
                break
            else:
                print("\n❌ Opção inválida!")
                input("\nPressione ENTER para continuar...")
    
    def tela_jogar(self):
        """Gerencia a tela de apostas e jogo."""
        self.limpar_tela()
        self.exibir_logo()
        
        print(f"\n💰 Saldo disponível: R$ {self._usuario_atual.get_saldo():.2f}")
        print("-" * 40)
        
        try:
            valor_aposta = float(input("\n💵 Digite o valor da aposta (ou 0 para voltar): R$ "))
            
            if valor_aposta == 0:
                return
            
            if valor_aposta < 0:
                print("\n❌ Erro: Valor inválido!")
                input("\nPressione ENTER para continuar...")
                return
            
            # Executa o jogo
            resultado = self._maquina.jogar(valor_aposta)
            
        except ValueError:
            print("\n❌ Erro: Digite um valor numérico válido!")
        
        input("\n\nPressione ENTER para continuar...")
    
    def tela_deposito(self):
        """Gerencia a tela de depósito."""
        self.limpar_tela()
        self.exibir_logo()
        
        print(f"\n💰 Saldo atual: R$ {self._usuario_atual.get_saldo():.2f}")
        print("-" * 40)
        
        try:
            valor = float(input("\n💵 Digite o valor do depósito (ou 0 para voltar): R$ "))
            
            if valor == 0:
                return
            
            if valor > 0:
                self._usuario_atual.depositar(valor)
            else:
                print("\n❌ Erro: Valor inválido!")
        
        except ValueError:
            print("\n❌ Erro: Digite um valor numérico válido!")
        
        input("\nPressione ENTER para continuar...")
    
    def tela_tabela_premios(self):
        """Exibe a tabela de prêmios."""
        self.limpar_tela()
        self.exibir_logo()
        
        self._maquina.exibir_tabela_premios()
        
        input("\n\nPressione ENTER para voltar...")
    
    def sair_e_salvar(self):
        """Salva o progresso e sai do jogo."""
        print("\n💾 Salvando seu progresso...")
        self._sistema_auth.atualizar_saldo(self._usuario_atual)
        print("✅ Progresso salvo com sucesso!")
        print(f"\n👋 Até logo, {self._usuario_atual.nome}!")
        self._usuario_atual = None
    
    def executar(self):
        """Executa o loop principal do jogo."""
        while True:
            self.limpar_tela()
            self.exibir_logo()
            
            opcao = self.menu_inicial()
            
            if opcao == "1":
                self.tela_login()
            elif opcao == "2":
                self.tela_cadastro()
            elif opcao == "3":
                print("\n👋 Obrigado por jogar! Até a próxima!")
                sys.exit(0)
            else:
                print("\n❌ Opção inválida!")
                input("\nPressione ENTER para continuar...")


def main():
    """Função principal que inicia o jogo."""
    jogo = JogoDoLeaozinho()
    jogo.executar()


if __name__ == "__main__":
    main()

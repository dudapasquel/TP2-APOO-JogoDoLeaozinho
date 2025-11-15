"""
Módulo que contém a classe Maquina.
Demonstra o conceito de Polimorfismo e composição de classes.
"""
import time
from .roleta import Roleta
from .usuario import Usuario
from .simbolo_especial import SimboloEspecial


class Maquina:
    """
    Classe principal do jogo que gerencia as 3 roletas.
    Controla o fluxo do jogo, apostas e cálculo de prêmios.
    """
    
    def __init__(self):
        """Inicializa a máquina com 3 roletas."""
        self._roleta1 = Roleta()
        self._roleta2 = Roleta()
        self._roleta3 = Roleta()
        self._valor_aposta = 0.0
        self._usuario_logado = None
    
    def definir_usuario(self, usuario: Usuario):
        """
        Define o usuário que está jogando.
        
        Args:
            usuario: Usuário logado
        """
        self._usuario_logado = usuario
    
    def jogar(self, valor_aposta: float) -> dict:
        """
        Executa uma rodada do jogo.
        
        Args:
            valor_aposta: Valor da aposta
            
        Returns:
            Dicionário com resultado do jogo (ganhou, premio, simbolos)
        """
        if not self._usuario_logado:
            print("❌ Erro: Nenhum usuário logado.")
            return {"ganhou": False, "premio": 0.0, "simbolos": []}
        
        # Valida se o usuário pode apostar
        if not self._usuario_logado.pode_apostar(valor_aposta):
            print(f"❌ Saldo insuficiente! Saldo atual: R$ {self._usuario_logado.get_saldo():.2f}")
            return {"ganhou": False, "premio": 0.0, "simbolos": []}
        
        # Debita a aposta do saldo
        self._valor_aposta = valor_aposta
        self._usuario_logado.sacar(valor_aposta)
        
        # Animação do giro
        print("\n🎰 Girando as roletas...")
        self._animar_giro()
        
        # Gira as 3 roletas
        simbolo1 = self._roleta1.girar()
        simbolo2 = self._roleta2.girar()
        simbolo3 = self._roleta3.girar()
        
        simbolos = [simbolo1, simbolo2, simbolo3]
        
        # Exibe o resultado
        self._exibir_resultado(simbolos)
        
        # Verifica se ganhou
        ganhou, premio = self._verificar_vitoria(simbolos)
        
        if ganhou:
            self._usuario_logado.depositar(premio)
            print(f"\n🎉 PARABÉNS! Você ganhou R$ {premio:.2f}!")
            print(f"💰 Saldo atual: R$ {self._usuario_logado.get_saldo():.2f}")
        else:
            print(f"\n😢 Não foi desta vez! Tente novamente!")
            print(f"💰 Saldo atual: R$ {self._usuario_logado.get_saldo():.2f}")
        
        return {
            "ganhou": ganhou,
            "premio": premio,
            "simbolos": simbolos
        }
    
    def _animar_giro(self):
        """Cria uma animação simples do giro das roletas."""
        animacao = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for _ in range(15):
            for frame in animacao:
                print(f"\r{frame} Girando... {frame}", end="", flush=True)
                time.sleep(0.05)
        print("\r" + " " * 50 + "\r", end="")  # Limpa a linha
    
    def _exibir_resultado(self, simbolos: list):
        """
        Exibe o resultado visual das 3 roletas.
        
        Args:
            simbolos: Lista com os 3 símbolos sorteados
        """
        print("\n╔═══════════════════════════════╗")
        print("║    🎰 RESULTADO DO GIRO 🎰    ║")
        print("╠═══════════════════════════════╣")
        print(f"║       {simbolos[0]}  |  {simbolos[1]}  |  {simbolos[2]}       ║")
        print("╚═══════════════════════════════╝")
    
    def _verificar_vitoria(self, simbolos: list) -> tuple[bool, float]:
        """
        Verifica se houve uma combinação vencedora e calcula o prêmio.
        Demonstra POLIMORFISMO: não precisa saber o tipo específico do símbolo,
        apenas chama o método calcular_premio que cada classe implementa.
        
        Args:
            simbolos: Lista com os 3 símbolos sorteados
            
        Returns:
            Tupla (ganhou: bool, premio: float)
        """
        simbolo1, simbolo2, simbolo3 = simbolos
        
        # Verifica se há coringas (Leão)
        coringas = [s for s in simbolos if isinstance(s, SimboloEspecial) and s.eh_coringa]
        
        # Caso 1: Todos os 3 símbolos são iguais (jackpot)
        if simbolo1.nome == simbolo2.nome == simbolo3.nome:
            # POLIMORFISMO: chama calcular_premio sem saber se é comum ou especial
            premio = simbolo1.calcular_premio(self._valor_aposta) * 3  # Prêmio triplo
            return True, premio
        
        # Caso 2: 2 símbolos iguais + 1 coringa
        if len(coringas) >= 1:
            # Identifica os símbolos não-coringa
            nao_coringas = [s for s in simbolos if not (isinstance(s, SimboloEspecial) and s.eh_coringa)]
            
            if len(nao_coringas) >= 2 and nao_coringas[0].nome == nao_coringas[1].nome:
                # POLIMORFISMO: calcular_premio funciona para qualquer tipo de símbolo
                premio = nao_coringas[0].calcular_premio(self._valor_aposta) * 2
                return True, premio
        
        # Caso 3: Apenas 2 símbolos iguais (sem coringa)
        if simbolo1.nome == simbolo2.nome or simbolo2.nome == simbolo3.nome or simbolo1.nome == simbolo3.nome:
            # Identifica qual símbolo se repetiu
            if simbolo1.nome == simbolo2.nome:
                simbolo_vencedor = simbolo1
            elif simbolo2.nome == simbolo3.nome:
                simbolo_vencedor = simbolo2
            else:
                simbolo_vencedor = simbolo1
            
            # POLIMORFISMO: não importa o tipo, apenas chama o método
            premio = simbolo_vencedor.calcular_premio(self._valor_aposta)
            return True, premio
        
        # Não ganhou
        return False, 0.0
    
    def exibir_tabela_premios(self):
        """Exibe a tabela de prêmios possíveis."""
        print("\n╔═══════════════════════════════════════════════════╗")
        print("║            📊 TABELA DE PRÊMIOS 📊                ║")
        print("╠═══════════════════════════════════════════════════╣")
        print("║  SÍMBOLOS COMUNS:                                 ║")
        print("║  🍒 Cereja   - 2x  (2 iguais) / 6x  (3 iguais)   ║")
        print("║  🍋 Limão    - 2.5x (2 iguais) / 7.5x (3 iguais) ║")
        print("║  🍊 Laranja  - 3x  (2 iguais) / 9x  (3 iguais)   ║")
        print("║  🍇 Uva      - 3.5x (2 iguais) / 10.5x (3 iguais)║")
        print("║  🍉 Melancia - 4x  (2 iguais) / 12x (3 iguais)   ║")
        print("║  🔔 Sino     - 5x  (2 iguais) / 15x (3 iguais)   ║")
        print("║  ⭐ Estrela  - 5x  (2 iguais) / 15x (3 iguais)   ║")
        print("║                                                   ║")
        print("║  SÍMBOLOS ESPECIAIS:                              ║")
        print("║  🦁 Leão     - 20x (2 iguais) / 60x (3 iguais)   ║")
        print("║               (Funciona como CORINGA!)            ║")
        print("║  💎 Diamante - 50x (2 iguais) / 150x (3 iguais)  ║")
        print("║               (JACKPOT MÁXIMO!)                   ║")
        print("╚═══════════════════════════════════════════════════╝")
    
    def __str__(self) -> str:
        """Retorna representação em string da máquina."""
        return f"🎰 Máquina Caça-níquel | Aposta atual: R$ {self._valor_aposta:.2f}"

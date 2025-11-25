import time
from .roleta import Roleta
from .usuario import Usuario
from .simbolo_especial import SimboloEspecial


class Maquina:
    
    def __init__(self):
        self._roleta1 = Roleta()
        self._roleta2 = Roleta()
        self._roleta3 = Roleta()
        self._valor_aposta = 0.0
        self._usuario_logado = None
    
    def definir_usuario(self, usuario: Usuario):
        self._usuario_logado = usuario
    
    def jogar(self, valor_aposta: float) -> dict:
        if not self._usuario_logado:
            print("❌ Erro: Nenhum usuário logado.")
            return {"ganhou": False, "premio": 0.0, "simbolos": []}
        
        if not self._usuario_logado.pode_apostar(valor_aposta):
            print(f"❌ Saldo insuficiente! Saldo atual: R$ {self._usuario_logado.get_saldo():.2f}")
            return {"ganhou": False, "premio": 0.0, "simbolos": []}
        
        self._valor_aposta = valor_aposta
        saldo_antes = self._usuario_logado.get_saldo()
        self._usuario_logado._Usuario__saldo -= valor_aposta
        self._usuario_logado._adicionar_transacao("Apostado", -valor_aposta)
        
        simbolo1 = self._roleta1.girar()
        simbolo2 = self._roleta2.girar()
        simbolo3 = self._roleta3.girar()
        
        simbolos = [simbolo1, simbolo2, simbolo3]
        
        self._exibir_resultado(simbolos)
        
        ganhou, premio = self._verificar_vitoria(simbolos)
        
        if ganhou:
            self._usuario_logado._Usuario__saldo += premio
            self._usuario_logado._adicionar_transacao("Ganho", premio)
            print(f"\n🎉 PARABÉNS! Você ganhou R$ {premio:.2f}!")
            print(f"💰 Saldo atual: R$ {self._usuario_logado.get_saldo():.2f}")
        else:
            print(f"\n😢 Não foi desta vez! Tente novamente!")
            print(f"💰 Saldo atual: R$ {self._usuario_logado.get_saldo():.2f}")
        
        self._usuario_logado.registrar_jogada(valor_aposta, premio if ganhou else 0, simbolos)
        
        return {
            "ganhou": ganhou,
            "premio": premio,
            "simbolos": simbolos
        }
    
    def _animar_giro(self):
        animacao = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for _ in range(15):
            for frame in animacao:
                print(f"\r{frame} Girando... {frame}", end="", flush=True)
                time.sleep(0.05)
        print("\r" + " " * 50 + "\r", end="")  # Limpa a linha
    
    def _exibir_resultado(self, simbolos: list):
        print("\n╔═══════════════════════════════╗")
        print("║    🎰 RESULTADO DO GIRO 🎰    ║")
        print("╠═══════════════════════════════╣")
        print(f"║       {simbolos[0]}  |  {simbolos[1]}  |  {simbolos[2]}       ║")
        print("╚═══════════════════════════════╝")
    
    def _verificar_vitoria(self, simbolos: list) -> tuple[bool, float]:
        simbolo1, simbolo2, simbolo3 = simbolos
        
        coringas = [s for s in simbolos if isinstance(s, SimboloEspecial) and s.eh_coringa]
        
        if simbolo1.nome == simbolo2.nome == simbolo3.nome:
            premio = simbolo1.calcular_premio(self._valor_aposta) * 3  # Prêmio triplo
            return True, premio
        
        if len(coringas) >= 1:
            nao_coringas = [s for s in simbolos if not (isinstance(s, SimboloEspecial) and s.eh_coringa)]
            
            if len(nao_coringas) >= 2 and nao_coringas[0].nome == nao_coringas[1].nome:
                premio = nao_coringas[0].calcular_premio(self._valor_aposta) * 2
                return True, premio
        
        if simbolo1.nome == simbolo2.nome or simbolo2.nome == simbolo3.nome or simbolo1.nome == simbolo3.nome:
            if simbolo1.nome == simbolo2.nome:
                simbolo_vencedor = simbolo1
            elif simbolo2.nome == simbolo3.nome:
                simbolo_vencedor = simbolo2
            else:
                simbolo_vencedor = simbolo1
            
            premio = simbolo_vencedor.calcular_premio(self._valor_aposta)
            return True, premio
        
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

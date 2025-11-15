"""
Módulo que contém a classe Roleta.
"""
import random
from .simbolo import Simbolo
from .simbolo_comum import SimboloComum
from .simbolo_especial import SimboloEspecial


class Roleta:
    """
    Classe que representa uma roleta do jogo.
    Contém símbolos e pode girar para retornar um símbolo aleatório.
    """
    
    def __init__(self):
        """Inicializa uma roleta com os símbolos disponíveis."""
        self._simbolos = self._criar_simbolos()
        self._resultado_atual = None
    
    def _criar_simbolos(self) -> list[Simbolo]:
        """
        Cria a lista de símbolos disponíveis na roleta.
        Demonstra a utilização de Herança e Polimorfismo.
        
        Returns:
            Lista de símbolos (comuns e especiais)
        """
        simbolos = []
        
        # Símbolos Comuns (maior probabilidade)
        simbolos_comuns = [
            SimboloComum("Cereja", "🍒", multiplicador=2.0),
            SimboloComum("Limão", "🍋", multiplicador=2.5),
            SimboloComum("Laranja", "🍊", multiplicador=3.0),
            SimboloComum("Uva", "🍇", multiplicador=3.5),
            SimboloComum("Melancia", "🍉", multiplicador=4.0),
            SimboloComum("Sino", "🔔", multiplicador=5.0),
            SimboloComum("Estrela", "⭐", multiplicador=5.0),
        ]
        
        # Adiciona múltiplas instâncias de símbolos comuns para aumentar probabilidade
        for simbolo in simbolos_comuns:
            simbolos.extend([simbolo] * 2)  # Cada símbolo comum aparece 2 vezes
        
        # Símbolos Especiais - Leão aparece mais!
        leao = SimboloEspecial("Leão", "🦁", multiplicador=20.0, eh_coringa=True)
        diamante = SimboloEspecial("Diamante", "💎", multiplicador=50.0, eh_coringa=False)
        
        # Leão aparece 4 vezes (mais comum que antes!)
        simbolos.extend([leao] * 4)
        
        # Diamante aparece 1 vez (raro)
        simbolos.append(diamante)
        
        return simbolos
    
    def girar(self) -> Simbolo:
        """
        Gira a roleta e retorna um símbolo aleatório.
        
        Returns:
            Símbolo sorteado
        """
        self._resultado_atual = random.choice(self._simbolos)
        return self._resultado_atual
    
    @property
    def resultado_atual(self) -> Simbolo:
        """Retorna o último resultado do giro."""
        return self._resultado_atual
    
    def __str__(self) -> str:
        """Retorna representação em string da roleta."""
        if self._resultado_atual:
            return str(self._resultado_atual)
        return "❓"

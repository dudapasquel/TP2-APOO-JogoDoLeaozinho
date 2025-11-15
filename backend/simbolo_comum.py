"""
Módulo que contém a classe SimboloComum.
Representa símbolos comuns do jogo (frutas, letras).
Demonstra o conceito de Herança.
"""

from .simbolo import Simbolo


class SimboloComum(Simbolo):
    """
    Classe que representa símbolos comuns do jogo (frutas, letras).
    Multiplicador padrão: 2x a 5x
    """
    
    def __init__(self, nome: str, icone: str, multiplicador: float = 2.0):
        """
        Inicializa um símbolo comum.
        
        Args:
            nome: Nome do símbolo
            icone: Representação visual do símbolo
            multiplicador: Multiplicador do prêmio (padrão: 2.0)
        """
        super().__init__(nome, icone)
        self._multiplicador = multiplicador
    
    def calcular_premio(self, valor_aposta: float) -> float:
        """
        Calcula o prêmio para símbolos comuns.
        Demonstra POLIMORFISMO: implementação específica do método abstrato.
        
        Args:
            valor_aposta: Valor apostado pelo jogador
            
        Returns:
            Valor do prêmio (aposta * multiplicador)
        """
        return valor_aposta * self._multiplicador
    
    @property
    def multiplicador(self) -> float:
        """Retorna o multiplicador do símbolo."""
        return self._multiplicador

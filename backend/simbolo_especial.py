"""
Módulo que contém a classe SimboloEspecial.
Representa símbolos especiais do jogo (Leão, Diamante).
Demonstra o conceito de Herança e Polimorfismo.
"""

from .simbolo import Simbolo


class SimboloEspecial(Simbolo):
    """
    Classe que representa símbolos especiais do jogo (Leão, Diamante).
    Símbolos especiais têm multiplicadores maiores e podem funcionar como coringa.
    Multiplicador especial: 10x a 50x
    """
    
    def __init__(self, nome: str, icone: str, multiplicador: float = 10.0, eh_coringa: bool = False):
        """
        Inicializa um símbolo especial.
        
        Args:
            nome: Nome do símbolo
            icone: Representação visual do símbolo
            multiplicador: Multiplicador do prêmio (padrão: 10.0)
            eh_coringa: Se o símbolo funciona como coringa
        """
        super().__init__(nome, icone)
        self._multiplicador = multiplicador
        self._eh_coringa = eh_coringa
    
    def calcular_premio(self, valor_aposta: float) -> float:
        """
        Calcula o prêmio para símbolos especiais.
        Demonstra POLIMORFISMO: implementação específica do método abstrato.
        Símbolos especiais têm multiplicadores muito maiores.
        
        Args:
            valor_aposta: Valor apostado pelo jogador
            
        Returns:
            Valor do prêmio (aposta * multiplicador especial)
        """
        return valor_aposta * self._multiplicador
    
    @property
    def multiplicador(self) -> float:
        """Retorna o multiplicador do símbolo."""
        return self._multiplicador
    
    @property
    def eh_coringa(self) -> bool:
        """Retorna se o símbolo é coringa."""
        return self._eh_coringa

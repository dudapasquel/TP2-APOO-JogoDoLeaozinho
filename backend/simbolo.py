"""
Módulo que contém a classe abstrata Simbolo.
Serve como base para SimboloComum e SimboloEspecial.
Demonstra o conceito de Classe Abstrata.
"""
from abc import ABC, abstractmethod


class Simbolo(ABC):
    """
    Classe abstrata que representa um símbolo genérico do jogo.
    Esta classe serve como contrato para as classes concretas.
    """
    
    def __init__(self, nome: str, icone: str):
        """
        Inicializa um símbolo.
        
        Args:
            nome: Nome do símbolo
            icone: Representação visual do símbolo
        """
        self._nome = nome
        self._icone = icone
    
    @property
    def nome(self) -> str:
        """Retorna o nome do símbolo."""
        return self._nome
    
    @property
    def icone(self) -> str:
        """Retorna o ícone do símbolo."""
        return self._icone
    
    @abstractmethod
    def calcular_premio(self, valor_aposta: float) -> float:
        """
        Método abstrato que calcula o prêmio baseado no valor da aposta.
        Cada tipo de símbolo terá sua própria implementação.
        
        Args:
            valor_aposta: Valor apostado pelo jogador
            
        Returns:
            Valor do prêmio calculado
        """
        pass
    
    def __str__(self) -> str:
        """Retorna representação em string do símbolo."""
        return self._icone
    
    def __repr__(self) -> str:
        """Retorna representação formal do símbolo."""
        return f"{self.__class__.__name__}(nome='{self._nome}', icone='{self._icone}')"

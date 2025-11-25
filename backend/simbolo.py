from abc import ABC, abstractmethod

class Simbolo(ABC):
    def __init__(self, nome: str, icone: str):
        self._nome = nome
        self._icone = icone
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def icone(self) -> str:
        return self._icone
    
    @abstractmethod
    def calcular_premio(self, valor_aposta: float) -> float:
        pass
    
    def __str__(self) -> str:
        return self._icone
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nome='{self._nome}', icone='{self._icone}')"

from .simbolo import Simbolo


class SimboloComum(Simbolo):
    
    def __init__(self, nome: str, icone: str, multiplicador: float = 2.0):
        super().__init__(nome, icone)
        self._multiplicador = multiplicador
    
    def calcular_premio(self, valor_aposta: float) -> float:
        return valor_aposta * self._multiplicador
    
    @property
    def multiplicador(self) -> float:
        return self._multiplicador

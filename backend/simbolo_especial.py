from .simbolo import Simbolo


class SimboloEspecial(Simbolo):

    def __init__(self, nome: str, icone: str, multiplicador: float = 10.0, eh_coringa: bool = False):
        super().__init__(nome, icone)
        self._multiplicador = multiplicador
        self._eh_coringa = eh_coringa
    
    def calcular_premio(self, valor_aposta: float) -> float:
        return valor_aposta * self._multiplicador
    
    @property
    def multiplicador(self) -> float:
        return self._multiplicador
    
    @property
    def eh_coringa(self) -> bool:
        return self._eh_coringa

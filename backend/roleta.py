import random
from .simbolo import Simbolo
from .simbolo_comum import SimboloComum
from .simbolo_especial import SimboloEspecial


class Roleta:
    
    def __init__(self):
        self._simbolos = self._criar_simbolos()
        self._resultado_atual = None
    
    def _criar_simbolos(self) -> list[Simbolo]:
        simbolos = []
        
        simbolos_comuns = [
            SimboloComum("Cereja", "🍒", multiplicador=2.0),
            SimboloComum("Limão", "🍋", multiplicador=2.5),
            SimboloComum("Laranja", "🍊", multiplicador=3.0),
            SimboloComum("Uva", "🍇", multiplicador=3.5),
            SimboloComum("Melancia", "🍉", multiplicador=4.0),
            SimboloComum("Sino", "🔔", multiplicador=5.0),
            SimboloComum("Estrela", "⭐", multiplicador=5.0),
        ]
        
        for simbolo in simbolos_comuns:
            simbolos.extend([simbolo] * 2)  # Cada símbolo comum aparece 2 vezes
        
        leao = SimboloEspecial("Leão", "🦁", multiplicador=20.0, eh_coringa=True)
        diamante = SimboloEspecial("Diamante", "💎", multiplicador=50.0, eh_coringa=False)
        
        simbolos.extend([leao] * 4)
        
        simbolos.append(diamante)
        
        return simbolos
    
    def girar(self) -> Simbolo:
        self._resultado_atual = random.choice(self._simbolos)
        return self._resultado_atual
    
    @property
    def resultado_atual(self) -> Simbolo:
        return self._resultado_atual
    
    def __str__(self) -> str:
        if self._resultado_atual:
            return str(self._resultado_atual)
        return "❓"

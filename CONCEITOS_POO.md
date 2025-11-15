# 📚 Conceitos de POO Aplicados no Projeto

## Índice
1. [Classes](#1-classes)
2. [Herança](#2-herança)
3. [Polimorfismo](#3-polimorfismo)
4. [Classe Abstrata](#4-classe-abstrata)
5. [Encapsulamento](#5-encapsulamento)

---

## 1. Classes

### Definição
Classes são "moldes" para criar objetos. Elas encapsulam dados (atributos) e comportamentos (métodos) relacionados.

### Implementação no Projeto

#### Classe `Usuario` (usuario.py)
```python
class Usuario:
    def __init__(self, nome: str, senha: str, saldo_inicial: float = 0.0):
        self._nome = nome
        self._senha = senha
        self.__saldo = saldo_inicial
```

**Atributos:**
- `_nome`: Nome do jogador
- `_senha`: Senha de acesso
- `__saldo`: Saldo virtual (privado)

**Métodos:**
- `depositar(valor)`: Adiciona créditos
- `sacar(valor)`: Remove créditos
- `get_saldo()`: Consulta saldo
- `verificar_senha(senha)`: Valida senha

#### Classe `Roleta` (roleta.py)
```python
class Roleta:
    def __init__(self):
        self._simbolos = self._criar_simbolos()
        self._resultado_atual = None
```

**Atributos:**
- `_simbolos`: Lista de símbolos disponíveis
- `_resultado_atual`: Último símbolo sorteado

**Métodos:**
- `girar()`: Sorteia um símbolo aleatório
- `_criar_simbolos()`: Inicializa os símbolos

#### Classe `Maquina` (maquina.py)
```python
class Maquina:
    def __init__(self):
        self._roleta1 = Roleta()
        self._roleta2 = Roleta()
        self._roleta3 = Roleta()
```

**Composição:** A Máquina **contém** 3 Roletas (relacionamento "tem-um")

**Métodos principais:**
- `jogar(valor_aposta)`: Executa uma rodada
- `_verificar_vitoria(simbolos)`: Verifica combinações vencedoras
- `exibir_tabela_premios()`: Mostra prêmios possíveis

---

## 2. Herança

### Definição
Herança permite que uma classe (filha) herde atributos e métodos de outra classe (pai), promovendo reutilização de código.

### Hierarquia no Projeto

```
         Simbolo (abstrata)
              |
      ________|________
     |                 |
SimboloComum    SimboloEspecial
```

### Implementação

#### Classe Pai: `Simbolo` (simbolo.py)
```python
from abc import ABC, abstractmethod

class Simbolo(ABC):
    def __init__(self, nome: str, icone: str):
        self._nome = nome
        self._icone = icone
    
    @abstractmethod
    def calcular_premio(self, valor_aposta: float) -> float:
        pass
```

#### Classe Filha: `SimboloComum`
```python
class SimboloComum(Simbolo):  # Herda de Simbolo
    def __init__(self, nome: str, icone: str, multiplicador: float = 2.0):
        super().__init__(nome, icone)  # Chama construtor da classe pai
        self._multiplicador = multiplicador
    
    def calcular_premio(self, valor_aposta: float) -> float:
        return valor_aposta * self._multiplicador
```

#### Classe Filha: `SimboloEspecial`
```python
class SimboloEspecial(Simbolo):  # Herda de Simbolo
    def __init__(self, nome: str, icone: str, multiplicador: float = 10.0, eh_coringa: bool = False):
        super().__init__(nome, icone)  # Chama construtor da classe pai
        self._multiplicador = multiplicador
        self._eh_coringa = eh_coringa
    
    def calcular_premio(self, valor_aposta: float) -> float:
        return valor_aposta * self._multiplicador
```

**Benefícios:**
- Código reutilizado (nome, icone)
- Especialização (multiplicadores diferentes)
- Extensibilidade (fácil adicionar novos tipos)

---

## 3. Polimorfismo

### Definição
Polimorfismo permite que objetos de classes diferentes sejam tratados através de uma interface comum, cada um respondendo de forma específica.

### Implementação no Projeto

#### Exemplo Prático (maquina.py)

```python
def _verificar_vitoria(self, simbolos: list) -> tuple[bool, float]:
    # simbolos pode conter SimboloComum OU SimboloEspecial
    simbolo1, simbolo2, simbolo3 = simbolos
    
    # POLIMORFISMO: Não precisa saber o tipo específico!
    # Ambos implementam calcular_premio(), mas de formas diferentes
    if simbolo1.nome == simbolo2.nome == simbolo3.nome:
        premio = simbolo1.calcular_premio(self._valor_aposta) * 3
        return True, premio
```

**Análise:**
- `simbolo1.calcular_premio()` pode chamar:
  - `SimboloComum.calcular_premio()` → `valor * 2.0 a 5.0`
  - `SimboloEspecial.calcular_premio()` → `valor * 10.0 a 50.0`
- O código **não precisa saber qual tipo** de símbolo é
- Funciona com qualquer classe que herde de `Simbolo`

#### Demonstração Visual

```python
# Todos são tratados como Simbolo
cereja = SimboloComum("Cereja", "🍒", multiplicador=2.0)
leao = SimboloEspecial("Leão", "🦁", multiplicador=20.0)

simbolos = [cereja, leao]

# Polimorfismo em ação
for simbolo in simbolos:
    premio = simbolo.calcular_premio(10.0)  # Mesmo método, resultados diferentes
    print(f"{simbolo.nome}: R${premio}")

# Saída:
# Cereja: R$20.00  (10 * 2)
# Leão: R$200.00   (10 * 20)
```

---

## 4. Classe Abstrata

### Definição
Uma classe abstrata é uma classe que **não pode ser instanciada diretamente**. Serve como um "contrato" que as classes filhas devem implementar.

### Implementação no Projeto

#### Classe `Simbolo` (simbolo.py)

```python
from abc import ABC, abstractmethod

class Simbolo(ABC):  # Herda de ABC (Abstract Base Class)
    
    @abstractmethod  # Decorator que marca método como abstrato
    def calcular_premio(self, valor_aposta: float) -> float:
        """Método que DEVE ser implementado pelas classes filhas"""
        pass
```

#### Por que usar?

1. **Não faz sentido ter um "Símbolo genérico"**
   ```python
   # Isso daria erro!
   simbolo = Simbolo("Genérico", "❓")  # TypeError
   ```

2. **Garante que classes filhas implementem métodos obrigatórios**
   ```python
   class SimboloNovo(Simbolo):
       # Se não implementar calcular_premio(), dá erro!
       pass  # TypeError: Can't instantiate abstract class
   ```

3. **Define um contrato**
   - Toda classe que herda de `Simbolo` **DEVE** ter `calcular_premio()`
   - Garante consistência no projeto

#### Tentativa de Instanciação (teste.py)

```python
# Isso funciona (classe concreta)
cereja = SimboloComum("Cereja", "🍒", 2.0)  ✅

# Isso NÃO funciona (classe abstrata)
simbolo = Simbolo("Teste", "❓")  ❌ TypeError
```

---

## 5. Encapsulamento

### Definição
Encapsulamento é o conceito de **esconder detalhes internos** de uma classe e expor apenas o que é necessário através de métodos públicos.

### Níveis de Acesso em Python

| Prefixo | Tipo | Acesso | Exemplo |
|---------|------|--------|---------|
| `nome` | Público | Qualquer lugar | `usuario.nome` |
| `_nome` | Protegido | Convenção (interno) | `self._nome` |
| `__nome` | Privado | Apenas dentro da classe | `self.__saldo` |

### Implementação no Projeto

#### Classe `Usuario` (usuario.py)

```python
class Usuario:
    def __init__(self, nome: str, senha: str, saldo_inicial: float = 0.0):
        self._nome = nome          # Protegido
        self._senha = senha        # Protegido
        self.__saldo = saldo_inicial  # PRIVADO (encapsulamento)
```

#### Por que `__saldo` é privado?

**Sem encapsulamento (RUIM):**
```python
usuario = Usuario("João", "123")
usuario.__saldo = -1000  # Poderia criar saldo negativo! ❌
usuario.__saldo = 999999  # Poderia trapacear! ❌
```

**Com encapsulamento (BOM):**
```python
usuario = Usuario("João", "123")

# Não consegue acessar diretamente
# usuario.__saldo = 1000  # AttributeError ❌

# Precisa usar métodos que fazem validações
usuario.depositar(100)   # Valida se valor > 0 ✅
usuario.sacar(50)        # Valida se tem saldo suficiente ✅
saldo = usuario.get_saldo()  # Acesso controlado ✅
```

#### Métodos Públicos de Acesso

```python
def get_saldo(self) -> float:
    """Acesso CONTROLADO ao saldo privado"""
    return self.__saldo

def depositar(self, valor: float) -> bool:
    """Modifica saldo COM VALIDAÇÃO"""
    if valor <= 0:
        print("❌ Erro: Valor deve ser positivo")
        return False
    self.__saldo += valor
    return True

def sacar(self, valor: float) -> bool:
    """Modifica saldo COM VALIDAÇÃO"""
    if self.__saldo < valor:
        print("❌ Erro: Saldo insuficiente")
        return False
    self.__saldo -= valor
    return True
```

#### Benefícios do Encapsulamento

1. **Proteção de Dados**
   - Saldo não pode ser negativo
   - Não pode ser alterado arbitrariamente

2. **Validação Centralizada**
   - Todas as alterações passam por validações
   - Mantém integridade dos dados

3. **Flexibilidade**
   - Pode mudar implementação interna sem afetar código externo
   - Exemplo: trocar `float` por classe `Dinheiro`

4. **Facilita Manutenção**
   - Bugs relacionados a saldo ficam concentrados
   - Fácil adicionar logs, auditorias, etc.

---

## 🎯 Resumo dos Conceitos

| Conceito | Onde | Por que |
|----------|------|---------|
| **Classes** | Todas as classes | Organizar dados e comportamentos |
| **Herança** | `Simbolo` → `SimboloComum/Especial` | Reutilizar código, especializar comportamento |
| **Polimorfismo** | `_verificar_vitoria()` | Tratar objetos diferentes uniformemente |
| **Classe Abstrata** | `Simbolo (ABC)` | Garantir contrato, evitar instância inválida |
| **Encapsulamento** | `Usuario.__saldo` | Proteger dados, validar alterações |

---

## 🔍 Como Identificar no Código

### Classes
```python
class NomeDaClasse:  # ← Definição de classe
    def __init__(self):  # ← Construtor
        self.atributo = valor  # ← Atributo
```

### Herança
```python
class Filha(Pai):  # ← Herda de Pai
    def __init__(self):
        super().__init__()  # ← Chama construtor do pai
```

### Polimorfismo
```python
for objeto in lista:
    objeto.mesmo_metodo()  # ← Mesmo método, comportamentos diferentes
```

### Classe Abstrata
```python
from abc import ABC, abstractmethod

class Abstrata(ABC):  # ← Herda de ABC
    @abstractmethod  # ← Método abstrato
    def metodo(self):
        pass
```

### Encapsulamento
```python
class Classe:
    def __init__(self):
        self.__privado = valor  # ← Privado (__)
    
    def get_privado(self):  # ← Getter público
        return self.__privado
```

---

**Desenvolvido para o TP2 de Programação Orientada a Objetos** 🎓

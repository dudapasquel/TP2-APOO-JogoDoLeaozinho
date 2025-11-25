from datetime import datetime


class Usuario:
    def __init__(self, nome: str, senha: str, saldo_inicial: float = 0.0, 
                 nome_completo: str = "", cpf: str = "", email: str = "", 
                 telefone: str = "", chave_pix: str = ""):
        self._nome = nome
        self._senha = senha
        self.__saldo = saldo_inicial 
        self._nome_completo = nome_completo
        self._cpf = cpf
        self._email = email
        self._telefone = telefone
        self._chave_pix = chave_pix
        self._historico_transacoes = [] 
        self._historico_jogadas = []
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def nome_completo(self) -> str:
        return self._nome_completo
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def telefone(self) -> str:
        return self._telefone
    
    @property
    def chave_pix(self) -> str:
        return self._chave_pix
    
    def atualizar_chave_pix(self, chave: str):
        self._chave_pix = chave
    
    def verificar_senha(self, senha: str) -> bool:
        return self._senha == senha
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("❌ Erro: O valor do depósito deve ser positivo.")
            return False
        
        self.__saldo += valor
        self._adicionar_transacao("Depósito", valor)
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"💰 Novo saldo: R$ {self.__saldo:.2f}")
        return True
    
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("❌ Erro: O valor do saque deve ser positivo.")
            return False
        
        if self.__saldo < valor:
            print(f"❌ Erro: Saldo insuficiente. Saldo atual: R$ {self.__saldo:.2f}")
            return False
        
        self.__saldo -= valor
        self._adicionar_transacao("Saque", -valor)
        return True
    
    def _adicionar_transacao(self, tipo: str, valor: float):
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "saldo_apos": self.__saldo
        }
        self._historico_transacoes.append(transacao)
    
    def registrar_jogada(self, aposta: float, premio: float, simbolos: list):
        jogada = {
            "aposta": aposta,
            "premio": premio,
            "lucro": premio - aposta,
            "simbolos": [s.nome for s in simbolos],
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self._historico_jogadas.append(jogada)
    
    def get_historico_transacoes(self) -> list:
        return self._historico_transacoes.copy()
    
    def get_historico_jogadas(self) -> list:
        return self._historico_jogadas.copy()
    
    def pode_apostar(self, valor_aposta: float) -> bool:
        return self.__saldo >= valor_aposta and valor_aposta > 0
    
    def __str__(self) -> str:
        return f"Usuário: {self._nome} | Saldo: R$ {self.__saldo:.2f}"
    
    def __repr__(self) -> str:
        return f"Usuario(nome='{self._nome}', saldo={self.__saldo})"

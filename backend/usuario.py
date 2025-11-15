"""
Módulo que contém a classe Usuario.
Demonstra o conceito de Encapsulamento.
"""


class Usuario:
    """
    Classe que representa um usuário/jogador do sistema.
    Demonstra encapsulamento através do atributo privado __saldo.
    """
    
    def __init__(self, nome: str, senha: str, saldo_inicial: float = 0.0):
        """
        Inicializa um usuário.
        
        Args:
            nome: Nome do usuário
            senha: Senha do usuário
            saldo_inicial: Saldo inicial do usuário (padrão: 0.0)
        """
        self._nome = nome
        self._senha = senha
        self.__saldo = saldo_inicial  # Atributo privado - encapsulamento
    
    @property
    def nome(self) -> str:
        """Retorna o nome do usuário."""
        return self._nome
    
    def verificar_senha(self, senha: str) -> bool:
        """
        Verifica se a senha fornecida está correta.
        
        Args:
            senha: Senha a ser verificada
            
        Returns:
            True se a senha estiver correta, False caso contrário
        """
        return self._senha == senha
    
    def get_saldo(self) -> float:
        """
        Retorna o saldo atual do usuário.
        Método público para acessar o atributo privado __saldo.
        
        Returns:
            Saldo atual do usuário
        """
        return self.__saldo
    
    def depositar(self, valor: float) -> bool:
        """
        Adiciona créditos ao saldo do usuário.
        Valida se o valor é positivo antes de depositar.
        
        Args:
            valor: Valor a ser depositado
            
        Returns:
            True se o depósito foi realizado, False caso contrário
        """
        if valor <= 0:
            print("❌ Erro: O valor do depósito deve ser positivo.")
            return False
        
        self.__saldo += valor
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        print(f"💰 Novo saldo: R$ {self.__saldo:.2f}")
        return True
    
    def sacar(self, valor: float) -> bool:
        """
        Remove créditos do saldo do usuário.
        Valida se há saldo suficiente antes de sacar.
        
        Args:
            valor: Valor a ser sacado
            
        Returns:
            True se o saque foi realizado, False caso contrário
        """
        if valor <= 0:
            print("❌ Erro: O valor do saque deve ser positivo.")
            return False
        
        if self.__saldo < valor:
            print(f"❌ Erro: Saldo insuficiente. Saldo atual: R$ {self.__saldo:.2f}")
            return False
        
        self.__saldo -= valor
        return True
    
    def pode_apostar(self, valor_aposta: float) -> bool:
        """
        Verifica se o usuário tem saldo suficiente para fazer a aposta.
        
        Args:
            valor_aposta: Valor da aposta
            
        Returns:
            True se pode apostar, False caso contrário
        """
        return self.__saldo >= valor_aposta and valor_aposta > 0
    
    def __str__(self) -> str:
        """Retorna representação em string do usuário."""
        return f"Usuário: {self._nome} | Saldo: R$ {self.__saldo:.2f}"
    
    def __repr__(self) -> str:
        """Retorna representação formal do usuário."""
        return f"Usuario(nome='{self._nome}', saldo={self.__saldo})"

"""
Módulo que gerencia a autenticação e cadastro de usuários.
"""
import json
import os
from .usuario import Usuario


class SistemaAutenticacao:
    """
    Classe responsável por gerenciar cadastro e login de usuários.
    Persiste dados em arquivo JSON.
    """
    
    def __init__(self, arquivo_dados: str = "usuarios.json"):
        """
        Inicializa o sistema de autenticação.
        
        Args:
            arquivo_dados: Caminho do arquivo para persistir usuários
        """
        self._arquivo_dados = arquivo_dados
        self._usuarios = self._carregar_usuarios()
    
    def _carregar_usuarios(self) -> dict:
        """
        Carrega os usuários do arquivo JSON.
        
        Returns:
            Dicionário com usuários {nome: {"senha": senha, "saldo": saldo}}
        """
        if not os.path.exists(self._arquivo_dados):
            return {}
        
        try:
            with open(self._arquivo_dados, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Aviso: Erro ao carregar dados de usuários. Criando novo arquivo.")
            return {}
    
    def _salvar_usuarios(self):
        """Salva os usuários no arquivo JSON."""
        try:
            with open(self._arquivo_dados, 'w', encoding='utf-8') as arquivo:
                json.dump(self._usuarios, arquivo, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"❌ Erro ao salvar dados: {e}")
    
    def cadastrar(self, nome: str, senha: str) -> bool:
        """
        Cadastra um novo usuário.
        
        Args:
            nome: Nome do usuário
            senha: Senha do usuário
            
        Returns:
            True se cadastro bem-sucedido, False caso contrário
        """
        # Validações
        if not nome or not senha:
            print("❌ Erro: Nome e senha não podem estar vazios.")
            return False
        
        if len(nome) < 3:
            print("❌ Erro: Nome deve ter pelo menos 3 caracteres.")
            return False
        
        if len(senha) < 4:
            print("❌ Erro: Senha deve ter pelo menos 4 caracteres.")
            return False
        
        if nome in self._usuarios:
            print("❌ Erro: Usuário já existe.")
            return False
        
        # Cadastra o usuário com bônus inicial de R$100
        self._usuarios[nome] = {
            "senha": senha,
            "saldo": 100.0
        }
        self._salvar_usuarios()
        print(f"✅ Usuário '{nome}' cadastrado com sucesso! Bônus de R$100,00 creditado!")
        return True
    
    def login(self, nome: str, senha: str) -> Usuario:
        """
        Realiza o login de um usuário.
        
        Args:
            nome: Nome do usuário
            senha: Senha do usuário
            
        Returns:
            Objeto Usuario se login bem-sucedido, None caso contrário
        """
        if nome not in self._usuarios:
            print("❌ Erro: Usuário não encontrado.")
            return None
        
        dados_usuario = self._usuarios[nome]
        
        if dados_usuario["senha"] != senha:
            print("❌ Erro: Senha incorreta.")
            return None
        
        # Cria objeto Usuario com os dados carregados
        usuario = Usuario(nome, senha, dados_usuario["saldo"])
        print(f"✅ Login realizado com sucesso! Bem-vindo, {nome}!")
        return usuario
    
    def atualizar_saldo(self, usuario: Usuario):
        """
        Atualiza o saldo do usuário no arquivo.
        
        Args:
            usuario: Usuário a ter o saldo atualizado
        """
        if usuario.nome in self._usuarios:
            self._usuarios[usuario.nome]["saldo"] = usuario.get_saldo()
            self._salvar_usuarios()
    
    def listar_usuarios(self) -> list:
        """
        Lista todos os usuários cadastrados (apenas nomes).
        
        Returns:
            Lista com nomes dos usuários
        """
        return list(self._usuarios.keys())

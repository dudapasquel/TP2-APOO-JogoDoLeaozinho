import json
import os
from .usuario import Usuario


class SistemaAutenticacao:
    def __init__(self, arquivo_dados: str = "usuarios.json"):
        self._arquivo_dados = arquivo_dados
        self._usuarios = self._carregar_usuarios()
    
    def _carregar_usuarios(self) -> dict:
        if not os.path.exists(self._arquivo_dados):
            return {}
        
        try:
            with open(self._arquivo_dados, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Aviso: Erro ao carregar dados de usuários. Criando novo arquivo.")
            return {}
    
    def _salvar_usuarios(self):
        try:
            with open(self._arquivo_dados, 'w', encoding='utf-8') as arquivo:
                json.dump(self._usuarios, arquivo, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"❌ Erro ao salvar dados: {e}")
    
    def cadastrar(self, nome: str, senha: str, nome_completo: str = "", 
                  cpf: str = "", email: str = "", telefone: str = "") -> bool:
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
        
        self._usuarios[nome] = {
            "senha": senha,
            "saldo": 10.0,
            "nome_completo": nome_completo,
            "cpf": cpf,
            "email": email,
            "telefone": telefone,
            "chave_pix": "",
            "historico_transacoes": [],
            "historico_jogadas": []
        }
        self._salvar_usuarios()
        print(f"✅ Usuário '{nome}' cadastrado com sucesso! Bônus de R$10,00 creditado!")
        return True
    
    def login(self, nome: str, senha: str) -> Usuario:
        if nome not in self._usuarios:
            print("❌ Erro: Usuário não encontrado.")
            return None
        
        dados_usuario = self._usuarios[nome]
        
        if dados_usuario["senha"] != senha:
            print("❌ Erro: Senha incorreta.")
            return None
        
        usuario = Usuario(
            nome=nome,
            senha=senha,
            saldo_inicial=dados_usuario.get("saldo", 100.0),
            nome_completo=dados_usuario.get("nome_completo", ""),
            cpf=dados_usuario.get("cpf", ""),
            email=dados_usuario.get("email", ""),
            telefone=dados_usuario.get("telefone", ""),
            chave_pix=dados_usuario.get("chave_pix", "")
        )
        
        usuario._historico_transacoes = dados_usuario.get("historico_transacoes", [])
        usuario._historico_jogadas = dados_usuario.get("historico_jogadas", [])
        
        print(f"✅ Login realizado com sucesso! Bem-vindo, {nome}!")
        return usuario
    
    def atualizar_saldo(self, usuario: Usuario):
        if usuario.nome in self._usuarios:
            self._usuarios[usuario.nome]["saldo"] = usuario.get_saldo()
            self._usuarios[usuario.nome]["historico_transacoes"] = usuario.get_historico_transacoes()
            self._usuarios[usuario.nome]["historico_jogadas"] = usuario.get_historico_jogadas()
            self._usuarios[usuario.nome]["chave_pix"] = usuario.chave_pix
            self._salvar_usuarios()
    
    def listar_usuarios(self) -> list:
        return list(self._usuarios.keys())

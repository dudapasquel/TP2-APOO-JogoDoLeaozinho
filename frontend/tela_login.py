"""
Tela de Login/Cadastro do Jogo do Leãozinho.
Primeira tela que o usuário vê ao iniciar o jogo.
"""

import customtkinter as ctk
import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path para importar backend
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend import Usuario, SistemaAutenticacao


class TelaLogin(ctk.CTk):
    """Tela principal de login/cadastro."""
    
    def __init__(self, callback_sucesso):
        super().__init__()
        
        self.callback_sucesso = callback_sucesso
        self.sistema_auth = SistemaAutenticacao("dados/usuarios.json")
        
        self.title("🦁 Jogo do Leãozinho - Login")
        self.geometry("500x650")
        self.resizable(False, False)
        
        # Centralizar janela na tela
        self._centralizar_janela()
        
        self._criar_interface()
    
    def _centralizar_janela(self):
        """Centraliza a janela na tela."""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def _criar_interface(self):
        """Cria os elementos da interface de login."""
        # Frame principal com degradê
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        frame_principal = ctk.CTkFrame(
            self,
            fg_color="#0f3460",
            corner_radius=0
        )
        frame_principal.grid(row=0, column=0, sticky="nsew")
        frame_principal.grid_columnconfigure(0, weight=1)
        
        # Logo com Leão
        logo_frame = ctk.CTkFrame(
            frame_principal,
            fg_color="transparent"
        )
        logo_frame.grid(row=0, column=0, pady=(50, 20), padx=20)
        
        # Múltiplos leões para dar destaque
        leoes = ctk.CTkLabel(
            logo_frame,
            text="🦁 🦁 🦁",
            font=("Arial", 60)
        )
        leoes.pack()
        
        # Título
        titulo = ctk.CTkLabel(
            frame_principal,
            text="JOGO DO LEÃOZINHO",
            font=("Arial Bold", 32),
            text_color="#d4af37"
        )
        titulo.grid(row=1, column=0, pady=10, padx=20)
        
        # Subtitle
        subtitulo = ctk.CTkLabel(
            frame_principal,
            text="🎰 Jogue com responsabilidade! 🎰",
            font=("Arial Bold", 20),
            text_color="#ffffff"
        )
        subtitulo.grid(row=2, column=0, pady=(0, 40), padx=20)
        
        # Frame do formulário
        form_frame = ctk.CTkFrame(
            frame_principal,
            fg_color="#1a1a2e",
            corner_radius=20,
            border_width=2,
            border_color="#d4af37"
        )
        form_frame.grid(row=3, column=0, pady=20, padx=50, sticky="ew")
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Campo de usuário
        self.entry_usuario = ctk.CTkEntry(
            form_frame,
            placeholder_text="👤 Nome de usuário",
            width=350,
            height=50,
            font=("Arial", 16),
            corner_radius=10
        )
        self.entry_usuario.grid(row=0, column=0, pady=(30, 15), padx=30)
        
        # Campo de senha
        self.entry_senha = ctk.CTkEntry(
            form_frame,
            placeholder_text="🔒 Senha",
            show="*",
            width=350,
            height=50,
            font=("Arial", 16),
            corner_radius=10
        )
        self.entry_senha.grid(row=1, column=0, pady=(0, 30), padx=30)
        
        # Botão de Login
        btn_login = ctk.CTkButton(
            frame_principal,
            text="🦁 ENTRAR NO JOGO 🦁",
            width=350,
            height=55,
            font=("Arial Bold", 18),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000000",
            corner_radius=15,
            command=self._fazer_login
        )
        btn_login.grid(row=4, column=0, pady=15, padx=50)
        
        # Botão de Cadastro
        btn_cadastro = ctk.CTkButton(
            frame_principal,
            text="📝 Criar Nova Conta",
            width=350,
            height=50,
            font=("Arial", 16),
            fg_color="transparent",
            hover_color="#16213e",
            border_width=2,
            border_color="#d4af37",
            corner_radius=15,
            command=self._fazer_cadastro
        )
        btn_cadastro.grid(row=5, column=0, pady=10, padx=50)
        
        # Label de mensagem
        self.label_mensagem = ctk.CTkLabel(
            frame_principal,
            text="",
            font=("Arial Bold", 13),
            text_color="#ff4444",
            wraplength=400
        )
        self.label_mensagem.grid(row=6, column=0, pady=15, padx=20)
        
        # Rodapé com informação
        rodape = ctk.CTkLabel(
            frame_principal,
            text="Bônus de R$ 100 para novos jogadores! 🎁",
            font=("Arial", 12),
            text_color="#44ff44"
        )
        rodape.grid(row=7, column=0, pady=(10, 20), padx=20)
        
        # Bind Enter key
        self.entry_senha.bind("<Return>", lambda e: self._fazer_login())
        self.entry_usuario.bind("<Return>", lambda e: self.entry_senha.focus())
    
    def _fazer_login(self):
        """Realiza o login."""
        nome = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        
        if not nome or not senha:
            self.label_mensagem.configure(
                text="❌ Preencha todos os campos!",
                text_color="#ff4444"
            )
            return
        
        usuario = self.sistema_auth.login(nome, senha)
        
        if usuario:
            self.label_mensagem.configure(
                text=f"✅ Bem-vindo, {nome}! Carregando jogo...",
                text_color="#44ff44"
            )
            self.after(500, lambda: self.callback_sucesso(usuario, self.sistema_auth))
        else:
            self.label_mensagem.configure(
                text="❌ Usuário ou senha incorretos!",
                text_color="#ff4444"
            )
            # Limpar senha
            self.entry_senha.delete(0, 'end')
    
    def _fazer_cadastro(self):
        """Realiza o cadastro."""
        nome = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        
        if not nome or not senha:
            self.label_mensagem.configure(
                text="❌ Preencha todos os campos!",
                text_color="#ff4444"
            )
            return
        
        if len(nome) < 3:
            self.label_mensagem.configure(
                text="❌ Nome deve ter pelo menos 3 caracteres!",
                text_color="#ff4444"
            )
            return
        
        if len(senha) < 4:
            self.label_mensagem.configure(
                text="❌ Senha deve ter pelo menos 4 caracteres!",
                text_color="#ff4444"
            )
            return
        
        if self.sistema_auth.cadastrar(nome, senha):
            # Deposito inicial de boas-vindas
            usuario = self.sistema_auth.login(nome, senha)
            if usuario:
                usuario.depositar(100.0)  # Bônus de boas-vindas
                self.sistema_auth.atualizar_saldo(usuario)
                
                self.label_mensagem.configure(
                    text="🎉 Conta criada! Você ganhou R$ 100 de bônus! Entrando...",
                    text_color="#44ff44"
                )
                self.after(1500, lambda: self.callback_sucesso(usuario, self.sistema_auth))
        else:
            self.label_mensagem.configure(
                text="❌ Usuário já existe! Tente outro nome.",
                text_color="#ff4444"
            )

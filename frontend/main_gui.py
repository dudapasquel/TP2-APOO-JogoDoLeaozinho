import customtkinter as ctk
from PIL import Image
import sys
import os
from pathlib import Path
from datetime import datetime
import re

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend import Usuario, Maquina, SistemaAutenticacao

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AplicacaoJogo(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("🦁 Jogo do Leãozinho")
        self.geometry("800x600")
        self.resizable(True, True)
        
        self.usuario = None
        self.sistema_auth = SistemaAutenticacao("dados/usuarios.json")
        self.maquina = Maquina()
        self.animacao_ativa = False
        self.imagens = {}
        self.tela_atual = "aviso"  
        self._carregar_imagens()
        
        self._criar_tela_aviso()
    
    def _validar_cpf(self, cpf: str) -> bool:
        cpf = re.sub(r'\D', '', cpf)
        
        if len(cpf) != 11:
            return False
        
        if cpf == cpf[0] * 11:
            return False
        
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10
        if int(cpf[9]) != digito1:
            return False
        
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10
        if int(cpf[10]) != digito2:
            return False
        
        return True
    
    def _validar_email(self, email: str) -> bool:
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
    
    def _validar_telefone(self, telefone: str) -> bool:
        telefone = re.sub(r'\D', '', telefone)
        return len(telefone) >= 10 and len(telefone) <= 11
    
    def _carregar_imagens(self):
        simbolos = [
            "cereja", "limao", "laranja", "uva", "melancia",
            "sino", "estrela", "leao", "diamante", "loading"
        ]
        
        for simbolo in simbolos:
            caminho = f"assets/simbolos/{simbolo}.png"
            if os.path.exists(caminho):
                img = Image.open(caminho)
                self.imagens[simbolo] = ctk.CTkImage(
                    light_image=img,
                    dark_image=img,
                    size=(100, 100)
                )
        
        self.gif_frames = []
        caminho_gif = "assets/roleta_girando.gif"
        if os.path.exists(caminho_gif):
            try:
                gif = Image.open(caminho_gif)
                for i in range(gif.n_frames):
                    gif.seek(i)
                    frame = gif.copy()
                    self.gif_frames.append(ctk.CTkImage(
                        light_image=frame,
                        dark_image=frame,
                        size=(100, 100)
                    ))
                gif.close()
            except Exception as e:
                print(f"⚠️ Erro ao carregar GIF: {e}")
                self.gif_frames = []
    
    def _limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def _criar_tela_aviso(self):
        self._limpar_tela()
        
        frame = ctk.CTkFrame(self, fg_color="#0f3460")
        frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            frame,
            text="⚠️ 🦁 ⚠️",
            font=("Arial", 50)
        ).pack(pady=(30, 10))
        
        ctk.CTkLabel(
            frame,
            text="JOGUE COM RESPONSABILIDADE",
            font=("Arial Bold", 22),
            text_color="#d4af37"
        ).pack(pady=10)
        
        avisos = [
            "• Este é um jogo de entretenimento",
            "• Jogue apenas o que você pode perder",
            "• Estabeleça limites de tempo e dinheiro",
            "• O jogo pode causar dependência",
            "• Procure ajuda se necessário",
            "",
            "Ao continuar, você confirma que:",
            "✓ Tem mais de 18 anos",
            "✓ Compreende os riscos",
            "✓ Jogará de forma responsável"
        ]
        
        for aviso in avisos:
            cor = "#44ff44" if "✓" in aviso else "#ffffff"
            ctk.CTkLabel(
                frame,
                text=aviso,
                font=("Arial", 12),
                text_color=cor
            ).pack(pady=2)
        
        ctk.CTkButton(
            frame,
            text="✓ Entendi e Desejo Continuar",
            width=250,
            height=50,
            font=("Arial Bold", 14),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=self._criar_tela_login
        ).pack(pady=20)
    
    def _criar_tela_login(self):
        self._limpar_tela()
        self.tela_atual = "login"
        
        frame = ctk.CTkFrame(self, fg_color="#0f3460")
        frame.pack(fill="both", expand=True)
        frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(
            frame,
            text="🦁 🦁 🦁",
            font=("Arial", 80)
        ).grid(row=0, column=0, pady=(60, 20))
        
        ctk.CTkLabel(
            frame,
            text="JOGO DO LEÃOZINHO",
            font=("Arial Bold", 36),
            text_color="#d4af37"
        ).grid(row=1, column=0, pady=10)
        
        form = ctk.CTkFrame(
            frame,
            fg_color="#1a1a2e",
            corner_radius=20,
            border_width=2,
            border_color="#d4af37"
        )
        form.grid(row=2, column=0, pady=30, padx=100, sticky="ew")
        
        ctk.CTkLabel(form, text="👤 Usuário:", font=("Arial", 16)).pack(pady=(30, 5), padx=40, anchor="w")
        self.entry_usuario = ctk.CTkEntry(form, placeholder_text="Digite seu usuário", width=350, height=45, font=("Arial", 14))
        self.entry_usuario.pack(pady=(0, 20), padx=40)
        
        ctk.CTkLabel(form, text="🔒 Senha:", font=("Arial", 16)).pack(pady=(10, 5), padx=40, anchor="w")
        self.entry_senha = ctk.CTkEntry(form, placeholder_text="Digite sua senha", width=350, height=45, font=("Arial", 14), show="•")
        self.entry_senha.pack(pady=(0, 20), padx=40)
        
        btn_frame = ctk.CTkFrame(form, fg_color="transparent")
        btn_frame.pack(pady=(0, 30))
        
        ctk.CTkButton(
            btn_frame,
            text="🦁 ENTRAR",
            width=170,
            height=50,
            font=("Arial Bold", 16),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=self._fazer_login
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text="📝 CADASTRAR",
            width=170,
            height=50,
            font=("Arial Bold", 16),
            command=self._criar_tela_cadastro
        ).pack(side="left", padx=5)
        
        ctk.CTkLabel(
            frame,
            text="🎁 Novos jogadores ganham R$10,00 de bônus! 🎁",
            font=("Arial Bold", 16),
            text_color="#44ff44"
        ).grid(row=3, column=0, pady=20)
        
        self.label_msg_login = ctk.CTkLabel(frame, text="", font=("Arial Bold", 14), text_color="#ff4444")
        self.label_msg_login.grid(row=4, column=0, pady=10)
        
        self.entry_senha.bind("<Return>", lambda e: self._fazer_login())
    
    def _fazer_login(self):
        nome = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        
        if not nome or not senha:
            self._mostrar_msg_temporaria(self.label_msg_login, "❌ Preencha todos os campos!")
            return
        
        usuario = self.sistema_auth.login(nome, senha)
        if usuario:
            print(f"✅ Login realizado com sucesso! Bem-vindo, {nome}!")
            self.usuario = usuario
            self.maquina.definir_usuario(usuario)
            self._criar_tela_jogo()
        else:
            self._mostrar_msg_temporaria(self.label_msg_login, "❌ Usuário ou senha incorretos!")

    def _criar_tela_cadastro(self):
        self._limpar_tela()
        self.tela_atual = "cadastro"
        
        frame = ctk.CTkScrollableFrame(self, fg_color="#0f3460")
        frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            frame,
            text="📝 CADASTRO COMPLETO",
            font=("Arial Bold", 36),
            text_color="#d4af37"
        ).pack(pady=30)
        
        ctk.CTkLabel(
            frame,
            text="Preencha todos os dados para continuar",
            font=("Arial", 16)
        ).pack(pady=(0, 30))
        
        form = ctk.CTkFrame(frame, fg_color="#1a1a2e", corner_radius=20, border_width=2, border_color="#d4af37")
        form.pack(pady=20, padx=100, fill="x")
        
        def criar_campo(label_text, placeholder, show=None):
            ctk.CTkLabel(form, text=label_text, font=("Arial", 16)).pack(pady=(20, 5), padx=40, anchor="w")
            entry = ctk.CTkEntry(form, placeholder_text=placeholder, width=400, height=45, font=("Arial", 14))
            if show:
                entry.configure(show=show)
            entry.pack(pady=(0, 10), padx=40)
            return entry
        
        self.entry_nome_completo = criar_campo("👤 Nome Completo:", "Nome completo")
        self.entry_cpf = criar_campo("📄 CPF:", "000.000.000-00")
        self.entry_email = criar_campo("📧 Email:", "seu@email.com")
        self.entry_telefone = criar_campo("📱 Telefone:", "(00) 00000-0000")
        self.entry_usuario_cad = criar_campo("🔑 Usuário:", "Digite um usuário")
        self.entry_senha_cad = criar_campo("🔒 Senha:", "Digite uma senha", "•")
        
        btn_frame = ctk.CTkFrame(form, fg_color="transparent")
        btn_frame.pack(pady=30)
        
        ctk.CTkButton(
            btn_frame,
            text="✓ Cadastrar",
            width=200,
            height=50,
            font=("Arial Bold", 16),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=self._processar_cadastro
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text="← Voltar",
            width=150,
            height=50,
            font=("Arial Bold", 16),
            command=self._criar_tela_login
        ).pack(side="left", padx=5)
        
        self.label_msg_cadastro = ctk.CTkLabel(frame, text="", font=("Arial Bold", 14), text_color="#ff4444")
        self.label_msg_cadastro.pack(pady=10)
    
    def _processar_cadastro(self):
        nome_completo = self.entry_nome_completo.get().strip()
        cpf = self.entry_cpf.get().strip().replace(".", "").replace("-", "")
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        usuario = self.entry_usuario_cad.get().strip()
        senha = self.entry_senha_cad.get().strip()
        
        if not all([nome_completo, cpf, email, telefone, usuario, senha]):
            self._mostrar_dialog("❌ Erro", "Todos os campos são obrigatórios!")
            return
        
        if not self._validar_cpf(cpf):
            self._mostrar_dialog("❌ CPF Inválido", "O CPF informado é inválido. Verifique os dígitos.")
            return
        
        if not self._validar_email(email):
            self._mostrar_dialog("❌ Email Inválido", "O email informado não é válido.\nExemplo: usuario@email.com")
            return
        
        if not self._validar_telefone(telefone):
            self._mostrar_dialog("❌ Telefone Inválido", "O telefone deve ter entre 10 e 11 dígitos.\nExemplo: (11) 98765-4321")
            return
            self._mostrar_msg_temporaria(self.label_msg_cadastro, "❌ Preencha todos os campos!")
            return
        
        if len(cpf) != 11 or not cpf.isdigit():
            self._mostrar_msg_temporaria(self.label_msg_cadastro, "❌ CPF inválido! Use 11 dígitos.")
            return
        
        if "@" not in email:
            self._mostrar_msg_temporaria(self.label_msg_cadastro, "❌ Email inválido!")
            return
        
        print(f"\n📝 === CADASTRANDO USUÁRIO ===")
        print(f"Nome: {nome_completo}")
        print(f"CPF: {cpf}")
        print(f"Email: {email}")
        print(f"Telefone: {telefone}")
        print(f"Usuário: {usuario}")
        
        if self.sistema_auth.cadastrar(usuario, senha, nome_completo, cpf, email, telefone):
            print("✅ Cadastro realizado com sucesso!")
            usr = self.sistema_auth.login(usuario, senha)
            if usr:
                self.usuario = usr
                self.maquina.definir_usuario(usr)
                self._criar_tela_jogo()
        else:
            print("❌ Erro: Usuário já existe.")
            self._mostrar_msg_temporaria(self.label_msg_cadastro, "❌ Usuário já existe!")

    def _criar_tela_jogo(self):
        self._limpar_tela()
        self.tela_atual = "jogo"
        self.valor_aposta = 10.0
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        header = ctk.CTkFrame(self, fg_color="#0f3460", corner_radius=0)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure((0, 1, 2), weight=1)
        
        ctk.CTkLabel(
            header,
            text="🦁 JOGO DO LEÃOZINHO 🦁",
            font=("Arial Bold", 32),
            text_color="#d4af37"
        ).grid(row=0, column=0, columnspan=3, pady=20)
        
        self.label_usuario = ctk.CTkLabel(header, text=f"👤 {self.usuario.nome}", font=("Arial", 16))
        self.label_usuario.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        
        self.label_saldo = ctk.CTkLabel(
            header,
            text=f"💰 Saldo: R$ {self.usuario.get_saldo():.2f}",
            font=("Arial Bold", 24),
            text_color="#44ff44"
        )
        self.label_saldo.grid(row=1, column=1, pady=10)
        
        btn_frame = ctk.CTkFrame(header, fg_color="transparent")
        btn_frame.grid(row=1, column=2, pady=10, padx=20, sticky="e")
        
        ctk.CTkButton(
            btn_frame,
            text="💵 Depositar",
            width=110,
            height=35,
            command=self._abrir_deposito
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text="💰 Sacar",
            width=110,
            height=35,
            fg_color="#44aa44",
            hover_color="#338833",
            command=self._criar_tela_saque
        ).pack(side="left", padx=5)
        
        frame_roletas = ctk.CTkFrame(self, fg_color="#1a1a2e")
        frame_roletas.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        frame_roletas.grid_columnconfigure((0, 1, 2), weight=1)
        
        container = ctk.CTkFrame(frame_roletas, fg_color="#16213e", corner_radius=20, border_width=3, border_color="#d4af37")
        container.grid(row=0, column=0, columnspan=3, pady=30, padx=50, sticky="nsew")
        container.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.roletas = []
        for i in range(3):
            frame_rol = ctk.CTkFrame(container, fg_color="#0f3460", corner_radius=15, width=180, height=180)
            frame_rol.grid(row=0, column=i, padx=20, pady=40)
            frame_rol.grid_propagate(False)
            
            label = ctk.CTkLabel(frame_rol, text="", image=self.imagens.get("loading"), width=150, height=150)
            label.place(relx=0.5, rely=0.5, anchor="center")
            self.roletas.append(label)
        
        controle = ctk.CTkFrame(self, fg_color="#16213e", corner_radius=15)
        controle.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        controle.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        ctk.CTkLabel(controle, text="Valor da Aposta:", font=("Arial", 16)).grid(row=0, column=0, pady=20, padx=10)
        
        ctk.CTkButton(
            controle,
            text="-",
            width=50,
            height=50,
            font=("Arial Bold", 24),
            command=self._diminuir_aposta
        ).grid(row=0, column=1, pady=20, padx=5)
        
        self.label_valor_aposta = ctk.CTkLabel(
            controle,
            text="R$ 10.00",
            font=("Arial Bold", 24),
            text_color="#d4af37",
            width=120
        )
        self.label_valor_aposta.grid(row=0, column=2, pady=20, padx=10)
        
        ctk.CTkButton(
            controle,
            text="+",
            width=50,
            height=50,
            font=("Arial Bold", 24),
            command=self._aumentar_aposta
        ).grid(row=0, column=3, pady=20, padx=5)
        
        self.btn_girar = ctk.CTkButton(
            controle,
            text="🦁 GIRAR 🦁",
            width=200,
            height=60,
            font=("Arial Bold", 22),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=self._girar_roletas
        )
        self.btn_girar.grid(row=0, column=4, pady=20, padx=20)
        
        footer = ctk.CTkFrame(self, fg_color="#0f3460", corner_radius=0, height=50)
        footer.grid(row=3, column=0, sticky="ew")
        footer.grid_columnconfigure((0, 1, 2), weight=1)
        
        ctk.CTkButton(
            footer,
            text="📊 Tabela de Prêmios",
            width=150,
            height=35,
            fg_color="transparent",
            command=self._mostrar_premios
        ).grid(row=0, column=0, pady=10, padx=20, sticky="w")
        
        ctk.CTkButton(
            footer,
            text="📜 Histórico",
            width=150,
            height=35,
            fg_color="transparent",
            command=self._criar_tela_historico
        ).grid(row=0, column=1, pady=10)
        
        ctk.CTkButton(
            footer,
            text="🚪 Sair",
            width=150,
            height=35,
            fg_color="#ff4444",
            hover_color="#cc0000",
            command=self._sair
        ).grid(row=0, column=2, pady=10, padx=20, sticky="e")
    
    def _aumentar_aposta(self):
        opcoes = [5.0, 10.0, 20.0, 50.0, 100.0]
        idx = opcoes.index(self.valor_aposta) if self.valor_aposta in opcoes else 0
        if idx < len(opcoes) - 1:
            self.valor_aposta = opcoes[idx + 1]
            self.label_valor_aposta.configure(text=f"R$ {self.valor_aposta:.2f}")
    
    def _diminuir_aposta(self):
        opcoes = [5.0, 10.0, 20.0, 50.0, 100.0]
        idx = opcoes.index(self.valor_aposta) if self.valor_aposta in opcoes else 1
        if idx > 0:
            self.valor_aposta = opcoes[idx - 1]
            self.label_valor_aposta.configure(text=f"R$ {self.valor_aposta:.2f}")
    
    def _girar_roletas(self):
        if self.animacao_ativa:
            return
        
        if self.usuario.get_saldo() < self.valor_aposta:
            self._mostrar_dialog("❌ Saldo Insuficiente", "Você não tem saldo suficiente para esta aposta!")
            return
        
        print(f"\n🎰 === NOVA JOGADA ===")
        print(f"💰 Aposta: R$ {self.valor_aposta:.2f}")
        
        self.animacao_ativa = True
        self.btn_girar.configure(state="disabled")
        
        resultado = self.maquina.jogar(self.valor_aposta)
        
        self._animar_com_gif(resultado)
    
    def _animar_com_gif(self, resultado):
        simbolos = resultado['simbolos']
        
        if hasattr(self, 'gif_frames') and self.gif_frames:
            for roleta in self.roletas:
                roleta.configure(image=self.gif_frames[0])
            
            self._animar_gif_frames(0, 40, lambda: self._mostrar_resultado_final(simbolos, resultado))
        else:
            self._mostrar_resultado_final(simbolos, resultado)
    
    def _animar_gif_frames(self, frame_idx, max_frames, callback):
        if frame_idx < max_frames and hasattr(self, 'gif_frames'):
            frame = self.gif_frames[frame_idx % len(self.gif_frames)]
            for roleta in self.roletas:
                roleta.configure(image=frame)
            self.after(50, lambda: self._animar_gif_frames(frame_idx + 1, max_frames, callback))
        else:
            callback()
    
    def _mostrar_resultado_final(self, simbolos, resultado):
        import unicodedata
        
        for i, roleta in enumerate(self.roletas):
            simbolo_nome = simbolos[i].nome.lower()
            
            nome_arquivo = ''.join(
                c for c in unicodedata.normalize('NFD', simbolo_nome)
                if unicodedata.category(c) != 'Mn'
            )
            
            if nome_arquivo in self.imagens:
                roleta.configure(image=self.imagens[nome_arquivo])
            else:
                print(f"⚠️ Imagem não encontrada para: {simbolo_nome} -> {nome_arquivo}")
        
        self.after(300, lambda: self._finalizar_jogada(resultado))
    
    def _finalizar_jogada(self, resultado):
        self._mostrar_resultado(resultado)
        self.animacao_ativa = False
        self.btn_girar.configure(state="normal")
    
    def _mostrar_resultado(self, resultado):
        self.label_saldo.configure(text=f"💰 Saldo: R$ {self.usuario.get_saldo():.2f}")
        
        if resultado['ganhou']:
            tem_leao = any(s.nome == "Leão" for s in resultado['simbolos'])
            if tem_leao:
                msg = f"🦁 LEÃO DA SORTE!\n\nGANHOU R$ {resultado['premio']:.2f}! 🦁"
            else:
                msg = f"🎉 PARABÉNS!\n\nVocê ganhou R$ {resultado['premio']:.2f}!"
            self._mostrar_dialog("✅ VOCÊ GANHOU!", msg)
        else:
            self._mostrar_dialog("😢 Não foi desta vez", "Tente novamente! A sorte está chegando! 🦁")
        
        self.sistema_auth.atualizar_saldo(self.usuario)
    
    def _criar_tela_saque(self):
        self._limpar_tela()
        self.tela_atual = "saque"
        
        frame = ctk.CTkFrame(self, fg_color="#0f3460")
        frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            frame,
            text="💰 SAQUE",
            font=("Arial Bold", 36),
            text_color="#d4af37"
        ).pack(pady=40)
        
        ctk.CTkLabel(
            frame,
            text=f"Saldo disponível: R$ {self.usuario.get_saldo():.2f}",
            font=("Arial", 18),
            text_color="#44ff44"
        ).pack(pady=5)
        
        ctk.CTkLabel(
            frame,
            text="⚠️ Saldo mínimo para saque: R$ 50,00",
            font=("Arial", 14),
            text_color="#ffaa00"
        ).pack(pady=5)
        
        form = ctk.CTkFrame(frame, fg_color="#1a1a2e", corner_radius=20, border_width=2, border_color="#d4af37")
        form.pack(pady=30, padx=150)
        
        ctk.CTkLabel(form, text="💵 Valor do Saque:", font=("Arial", 16)).pack(pady=(30, 5), padx=40, anchor="w")
        self.entry_valor_saque = ctk.CTkEntry(form, placeholder_text="Digite o valor", width=400, height=45, font=("Arial", 14))
        self.entry_valor_saque.pack(pady=(0, 20), padx=40)
        
        ctk.CTkLabel(form, text="🔑 Chave PIX:", font=("Arial", 16)).pack(pady=(10, 5), padx=40, anchor="w")
        ctk.CTkLabel(form, text="Use seu CPF, email ou telefone cadastrado", font=("Arial", 11), text_color="#aaaaaa").pack(pady=(0, 5), padx=40, anchor="w")
        self.entry_chave_pix = ctk.CTkEntry(form, placeholder_text="Digite sua chave PIX", width=400, height=45, font=("Arial", 14))
        
        if hasattr(self.usuario, 'chave_pix') and self.usuario.chave_pix:
            self.entry_chave_pix.insert(0, self.usuario.chave_pix)
        
        self.entry_chave_pix.pack(pady=(0, 30), padx=40)
        
        btn_frame = ctk.CTkFrame(form, fg_color="transparent")
        btn_frame.pack(pady=(0, 30))
        
        ctk.CTkButton(
            btn_frame,
            text="✓ Confirmar Saque",
            width=200,
            height=50,
            font=("Arial Bold", 16),
            fg_color="#44aa44",
            hover_color="#338833",
            command=self._processar_saque
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text="← Cancelar",
            width=150,
            height=50,
            font=("Arial Bold", 16),
            command=self._criar_tela_jogo
        ).pack(side="left", padx=5)
        
        self.label_msg_saque = ctk.CTkLabel(frame, text="", font=("Arial Bold", 14), text_color="#ff4444")
        self.label_msg_saque.pack(pady=10)
    
    def _processar_saque(self):
        valor_str = self.entry_valor_saque.get().strip()
        chave_pix = self.entry_chave_pix.get().strip()
        
        print(f"\n💸 === PROCESSANDO SAQUE ===")
        print(f"Valor digitado: '{valor_str}'")
        print(f"Chave PIX digitada: '{chave_pix}'")
        
        if self.usuario.get_saldo() < 50.0:
            print(f"❌ Erro: Saldo mínimo não atingido. Saldo atual: R$ {self.usuario.get_saldo():.2f}")
            self._mostrar_dialog("❌ Saldo Insuficiente", f"Você precisa ter no mínimo R$ 50,00 para realizar um saque.\n\nSeu saldo atual: R$ {self.usuario.get_saldo():.2f}")
            return
        
        if not chave_pix:
            print("❌ Erro: Chave PIX não informada")
            self._mostrar_dialog("❌ Chave PIX Necessária", "Por favor, informe sua chave PIX para realizar o saque.")
            return
        
        cpf_usuario = self.usuario.cpf.replace(".", "").replace("-", "").strip()
        email_usuario = self.usuario.email.strip().lower()
        telefone_usuario = self.usuario.telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").strip()
        chave_pix_limpa = chave_pix.replace(".", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "").strip().lower()
        
        chave_valida = False
        tipo_chave = ""
        if cpf_usuario and chave_pix_limpa == cpf_usuario:
            chave_valida = True
            tipo_chave = "CPF"
            print(f"✓ Chave PIX válida: CPF corresponde")
        elif email_usuario and chave_pix_limpa == email_usuario:
            chave_valida = True
            tipo_chave = "Email"
            print(f"✓ Chave PIX válida: Email corresponde")
        elif telefone_usuario and chave_pix_limpa == telefone_usuario:
            chave_valida = True
            tipo_chave = "Telefone"
            print(f"✓ Chave PIX válida: Telefone corresponde")
        
        if not chave_valida:
            print("❌ Erro: Chave PIX não corresponde aos dados cadastrados")
            self._mostrar_dialog(
                "❌ Chave PIX Inválida", 
                f"A chave PIX deve ser um dos seus dados cadastrados:\n\n"
                f"• CPF: {self.usuario.cpf if self.usuario.cpf else 'Não cadastrado'}\n"
                f"• Email: {self.usuario.email if self.usuario.email else 'Não cadastrado'}\n"
                f"• Telefone: {self.usuario.telefone if self.usuario.telefone else 'Não cadastrado'}\n\n"
                f"⚠️ Não é permitido saque para conta de terceiros!"
            )
            return
        
        try:
            valor = float(valor_str)
            print(f"Valor convertido: R$ {valor:.2f}")
            
            if valor <= 0:
                print("❌ Erro: Valor deve ser positivo")
                self._mostrar_dialog("❌ Valor Inválido", "O valor do saque deve ser maior que zero.")
                return
            
            if valor > self.usuario.get_saldo():
                print(f"❌ Erro: Saldo insuficiente. Saldo: R$ {self.usuario.get_saldo():.2f}")
                self._mostrar_dialog("❌ Saldo Insuficiente", f"Você não tem saldo suficiente.\n\nSaldo disponível: R$ {self.usuario.get_saldo():.2f}\nValor solicitado: R$ {valor:.2f}")
                return
            
            if self.usuario.sacar(valor):
                self.usuario.atualizar_chave_pix(chave_pix)
                self.sistema_auth.atualizar_saldo(self.usuario)
                print(f"✅ Saque realizado com sucesso!")
                print(f"Chave PIX ({tipo_chave}): {chave_pix}")
                self._mostrar_dialog("✅ Saque Realizado", f"Saque de R$ {valor:.2f} realizado com sucesso!\n\nO valor será enviado para sua chave PIX ({tipo_chave}).")
                self._criar_tela_jogo()
        except ValueError:
            print("❌ Erro: Valor não é um número válido")
            self._mostrar_dialog("❌ Valor Inválido", "Por favor, digite um valor numérico válido.")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            self._mostrar_dialog("❌ Erro", f"Ocorreu um erro ao processar o saque.\n\nTente novamente.")
    
    def _criar_tela_historico(self):
        self._limpar_tela()
        self.tela_atual = "historico"
        
        frame = ctk.CTkFrame(self, fg_color="#0f3460")
        frame.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            frame,
            text="📜 HISTÓRICO",
            font=("Arial Bold", 28),
            text_color="#d4af37"
        ).pack(pady=20)
        
        tab_frame = ctk.CTkFrame(frame, fg_color="transparent")
        tab_frame.pack(pady=10)
        
        self.btn_tab_transacoes = ctk.CTkButton(
            tab_frame,
            text="💰 Transações",
            width=180,
            height=35,
            font=("Arial Bold", 14),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=lambda: self._trocar_tab_historico("transacoes")
        )
        self.btn_tab_transacoes.pack(side="left", padx=10)
        
        self.btn_tab_jogadas = ctk.CTkButton(
            tab_frame,
            text="🎰 Jogadas",
            width=180,
            height=35,
            font=("Arial Bold", 14),
            command=lambda: self._trocar_tab_historico("jogadas")
        )
        self.btn_tab_jogadas.pack(side="left", padx=10)
        
        self.frame_historico_conteudo = ctk.CTkScrollableFrame(
            frame,
            fg_color="#1a1a2e",
            corner_radius=20,
            border_width=2,
            border_color="#d4af37",
            width=700,
            height=300
        )
        self.frame_historico_conteudo.pack(pady=15, padx=20, fill="both", expand=True)
        
        ctk.CTkButton(
            frame,
            text="← Voltar ao Jogo",
            width=180,
            height=40,
            font=("Arial Bold", 14),
            command=self._criar_tela_jogo
        ).pack(pady=15)
        
        self.tab_historico_atual = "transacoes"
        self._atualizar_historico()
    
    def _trocar_tab_historico(self, tab):
        self.tab_historico_atual = tab
        
        if tab == "transacoes":
            self.btn_tab_transacoes.configure(fg_color="#d4af37", text_color="#000")
            self.btn_tab_jogadas.configure(fg_color="#16213e", text_color="#ffffff")
        else:
            self.btn_tab_transacoes.configure(fg_color="#16213e", text_color="#ffffff")
            self.btn_tab_jogadas.configure(fg_color="#d4af37", text_color="#000")
        
        self._atualizar_historico()
    
    def _atualizar_historico(self):
        for widget in self.frame_historico_conteudo.winfo_children():
            widget.destroy()
        
        if self.tab_historico_atual == "transacoes":
            self._mostrar_historico_transacoes()
        else:
            self._mostrar_historico_jogadas()
    
    def _mostrar_historico_transacoes(self):
        try:
            transacoes = self.usuario.get_historico_transacoes()
        except:
            transacoes = []
        
        if not transacoes:
            ctk.CTkLabel(
                self.frame_historico_conteudo,
                text="Nenhuma transação registrada ainda.",
                font=("Arial", 16)
            ).pack(pady=50)
            return
        
        header = ctk.CTkFrame(self.frame_historico_conteudo, fg_color="#0f3460")
        header.pack(fill="x", pady=(10, 20), padx=10)
        
        ctk.CTkLabel(header, text="Data/Hora", font=("Arial Bold", 14), width=200).pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(header, text="Tipo", font=("Arial Bold", 14), width=150).pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(header, text="Valor", font=("Arial Bold", 14), width=150).pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(header, text="Saldo Após", font=("Arial Bold", 14), width=150).pack(side="left", padx=10, pady=10)
        
        for trans in reversed(transacoes[-20:]): 
            item = ctk.CTkFrame(self.frame_historico_conteudo, fg_color="#16213e")
            item.pack(fill="x", pady=5, padx=10)
            
            data_hora = trans.get('data', 'N/A')
            tipo = trans.get('tipo', 'N/A')
            valor = trans.get('valor', 0)
            saldo_apos = trans.get('saldo_apos', 0)
            
            if tipo.upper() == "DEPÓSITO":
                cor_tipo = "#44ff44"
            elif tipo.upper() == "GANHO":
                cor_tipo = "#ffdd44"
            elif tipo.upper() == "APOSTADO":
                cor_tipo = "#ff8844"
            else: 
                cor_tipo = "#ff4444"
            
            ctk.CTkLabel(item, text=data_hora, font=("Arial", 12), width=200).pack(side="left", padx=10, pady=10)
            ctk.CTkLabel(item, text=tipo, font=("Arial Bold", 12), text_color=cor_tipo, width=150).pack(side="left", padx=10, pady=10)
            ctk.CTkLabel(item, text=f"R$ {valor:.2f}", font=("Arial", 12), width=150).pack(side="left", padx=10, pady=10)
            ctk.CTkLabel(item, text=f"R$ {saldo_apos:.2f}", font=("Arial", 12), width=150).pack(side="left", padx=10, pady=10)
    
    def _mostrar_historico_jogadas(self):
        try:
            jogadas = self.usuario.get_historico_jogadas()
        except:
            jogadas = []
        
        if not jogadas:
            ctk.CTkLabel(
                self.frame_historico_conteudo,
                text="Nenhuma jogada registrada ainda.",
                font=("Arial", 16)
            ).pack(pady=50)
            return
        
        header = ctk.CTkFrame(self.frame_historico_conteudo, fg_color="#0f3460")
        header.pack(fill="x", pady=(10, 20), padx=10)
        
        ctk.CTkLabel(header, text="Data/Hora", font=("Arial Bold", 14), width=180).pack(side="left", padx=5, pady=10)
        ctk.CTkLabel(header, text="Aposta", font=("Arial Bold", 14), width=100).pack(side="left", padx=5, pady=10)
        ctk.CTkLabel(header, text="Símbolos", font=("Arial Bold", 14), width=250).pack(side="left", padx=5, pady=10)
        ctk.CTkLabel(header, text="Prêmio", font=("Arial Bold", 14), width=100).pack(side="left", padx=5, pady=10)
        ctk.CTkLabel(header, text="Lucro", font=("Arial Bold", 14), width=100).pack(side="left", padx=5, pady=10)
        
        for jog in reversed(jogadas[-20:]):
            item = ctk.CTkFrame(self.frame_historico_conteudo, fg_color="#16213e")
            item.pack(fill="x", pady=5, padx=10)
            
            data_hora = jog.get('data', 'N/A')
            aposta = jog.get('aposta', 0)
            simbolos = jog.get('simbolos', [])
            premio = jog.get('premio', 0)
            lucro = jog.get('lucro', 0)
            
            simbolos_str = " | ".join(simbolos) if simbolos else "N/A"
            cor_lucro = "#44ff44" if lucro > 0 else ("#ff4444" if lucro < 0 else "#ffffff")
            
            ctk.CTkLabel(item, text=data_hora, font=("Arial", 11), width=180).pack(side="left", padx=5, pady=10)
            ctk.CTkLabel(item, text=f"R$ {aposta:.2f}", font=("Arial", 11), width=100).pack(side="left", padx=5, pady=10)
            ctk.CTkLabel(item, text=simbolos_str, font=("Arial", 11), width=250).pack(side="left", padx=5, pady=10)
            ctk.CTkLabel(item, text=f"R$ {premio:.2f}", font=("Arial", 11), width=100).pack(side="left", padx=5, pady=10)
            ctk.CTkLabel(item, text=f"R$ {lucro:+.2f}", font=("Arial Bold", 11), text_color=cor_lucro, width=100).pack(side="left", padx=5, pady=10)
    
    def _abrir_deposito(self):
        dialog = ctk.CTkInputDialog(
            text="Digite o valor do depósito (R$):",
            title="💵 Depositar"
        )
        
        valor_str = dialog.get_input()
        if valor_str:
            try:
                valor = float(valor_str)
                if valor > 0:
                    self.usuario.depositar(valor)
                    self.sistema_auth.atualizar_saldo(self.usuario)
                    self.label_saldo.configure(text=f"💰 Saldo: R$ {self.usuario.get_saldo():.2f}")
                    self._mostrar_dialog("✅ Depósito Realizado", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                else:
                    self._mostrar_dialog("❌ Erro", "Valor deve ser positivo!")
            except ValueError:
                self._mostrar_dialog("❌ Erro", "Valor inválido!")
    
    def _mostrar_premios(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("📊 Tabela de Prêmios")
        dialog.geometry("700x650")
        dialog.transient(self)
        dialog.grab_set()
        
        ctk.CTkLabel(
            dialog,
            text="📊 TABELA DE PRÊMIOS",
            font=("Arial Bold", 28),
            text_color="#d4af37"
        ).pack(pady=20)
        
        frame = ctk.CTkScrollableFrame(dialog, fg_color="#1a1a2e")
        frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        ctk.CTkLabel(
            frame,
            text="💡 Combinações de 3 símbolos pagam 3x | 2 símbolos pagam 1x | 2 símbolos + 🦁 pagam 2x",
            font=("Arial", 12),
            text_color="#ffaa00",
            wraplength=600
        ).pack(pady=10)
        
        premios = [
            ("🦁 🦁 🦁 3 Leões", "60x", "(20 × 3)"),
            ("💎 💎 💎 3 Diamantes", "150x", "(50 × 3)"),
            ("⭐ ⭐ ⭐ 3 Estrelas", "15x", "(5 × 3)"),
            ("🔔 🔔 🔔 3 Sinos", "15x", "(5 × 3)"),
            ("🍉 🍉 🍉 3 Melancias", "12x", "(4 × 3)"),
            ("🍇 🍇 🍇 3 Uvas", "10.5x", "(3.5 × 3)"),
            ("🍊 🍊 🍊 3 Laranjas", "9x", "(3 × 3)"),
            ("🍋 🍋 🍋 3 Limões", "7.5x", "(2.5 × 3)"),
            ("🍒 🍒 🍒 3 Cerejas", "6x", "(2 × 3)"),
            ("", "", ""),
            ("🦁 🦁 Qualquer | 2 Leões", "20x", "(20 × 1)"),
            ("💎 💎 Qualquer | 2 Diamantes", "50x", "(50 × 1)"),
            ("⭐ ⭐ Qualquer | 2 Estrelas", "5x", "(5 × 1)"),
            ("🔔 🔔 Qualquer | 2 Sinos", "5x", "(5 × 1)"),
            ("🍉 🍉 Qualquer | 2 Melancias", "4x", "(4 × 1)"),
            ("", "", ""),
            ("🦁 Coringa", "🦁 = Qualquer símbolo", "2x bônus"),
        ]
        
        for item_data in premios:
            if len(item_data) == 3:
                simbolo, mult, calc = item_data
            else:
                simbolo, mult = item_data
                calc = ""
            
            if not simbolo:
                ctk.CTkLabel(frame, text="", height=10).pack()
                continue
            
            item = ctk.CTkFrame(frame, fg_color="#16213e")
            item.pack(fill="x", pady=5, padx=10)
            
            ctk.CTkLabel(
                item,
                text=simbolo,
                font=("Arial Bold", 16),
                width=280,
                anchor="w"
            ).pack(side="left", padx=15, pady=12)
            
            if calc:
                ctk.CTkLabel(
                    item,
                    text=calc,
                    font=("Arial", 11),
                    text_color="#888888",
                    width=80
                ).pack(side="right", padx=5)
            
            ctk.CTkLabel(
                item,
                text=mult,
                font=("Arial Bold", 18),
                text_color="#44ff44",
                width=80
            ).pack(side="right", padx=10, pady=12)
        
        ctk.CTkButton(
            dialog,
            text="Fechar",
            width=200,
            height=40,
            command=dialog.destroy
        ).pack(pady=10)
    
    def _mostrar_dialog(self, titulo, mensagem):
        dialog = ctk.CTkToplevel(self)
        dialog.title(titulo)
        dialog.geometry("500x250")
        dialog.transient(self)
        dialog.grab_set()
        
        ctk.CTkLabel(
            dialog,
            text=mensagem,
            font=("Arial", 18),
            wraplength=450
        ).pack(pady=50)
        
        ctk.CTkButton(
            dialog,
            text="OK",
            width=150,
            height=40,
            font=("Arial Bold", 16),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=dialog.destroy
        ).pack(pady=20)
    
    def _mostrar_msg_temporaria(self, label, mensagem, tempo=3000):
        label.configure(text=mensagem)
        self.after(tempo, lambda: label.configure(text=""))
    
    def _sair(self):
        if self.usuario:
            self.sistema_auth.atualizar_saldo(self.usuario)
            self.usuario = None
            self.maquina = Maquina()
        self._criar_tela_login()


def main():
    app = AplicacaoJogo()
    app.mainloop()


if __name__ == "__main__":
    main()

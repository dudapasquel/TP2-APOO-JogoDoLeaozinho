"""
Interface gráfica principal do Jogo do Leãozinho usando CustomTkinter.
Implementa a interface moderna com 3 roletas animadas.
"""

import customtkinter as ctk
from PIL import Image
import sys
import os
from pathlib import Path

# Adicionar o diretório raiz ao path para importar backend
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend import Usuario, Maquina, SistemaAutenticacao


# Configuração do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AplicacaoJogo(ctk.CTk):
    """Aplicação principal do jogo com interface gráfica."""
    
    def __init__(self):
        super().__init__()
        
        self.title("🦁 Jogo do Leãozinho")
        self.geometry("1400x900")
        self.resizable(True, True)
        
        self.update_idletasks()
        width = 700
        height = 450
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        # Variáveis
        self.usuario = None
        self.sistema_auth = SistemaAutenticacao("dados/usuarios.json")
        self.maquina = Maquina()
        self.animacao_ativa = False
        self.imagens = {}
        self.logado = False
        
        # Carregar imagens
        self._carregar_imagens()
        
        # Criar interface de login primeiro
        self._criar_interface_login()
    
    def _carregar_imagens(self):
        """Carrega todas as imagens dos símbolos."""
        simbolos = [
            "cereja", "limao", "laranja", "uva", "melancia",
            "sino", "estrela", "leao", "diamante", "loading"
        ]
        
        for simbolo in simbolos:
            caminho = f"assets/simbolos/{simbolo}.png"
            if os.path.exists(caminho):
                self.imagens[simbolo] = ctk.CTkImage(
                    light_image=Image.open(caminho),
                    dark_image=Image.open(caminho),
                    size=(150, 150)
                )
            else:
                print(f"⚠️ Imagem não encontrada: {caminho}")
    
    def _criar_interface_login(self):
        """Cria a interface de login/cadastro."""
        # Frame principal
        self.frame_login = ctk.CTkFrame(self, fg_color="#0f3460")
        self.frame_login.pack(fill="both", expand=True)
        self.frame_login.grid_columnconfigure(0, weight=1)
        
        # Logo
        logo = ctk.CTkLabel(
            self.frame_login,
            text="🦁 🦁 🦁",
            font=("Arial", 80)
        )
        logo.grid(row=0, column=0, pady=(80, 20))
        
        # Título
        titulo = ctk.CTkLabel(
            self.frame_login,
            text="JOGO DO LEÃOZINHO",
            font=("Arial Bold", 36),
            text_color="#d4af37"
        )
        titulo.grid(row=1, column=0, pady=10)
        
        # Frame do formulário
        form_frame = ctk.CTkFrame(
            self.frame_login,
            fg_color="#1a1a2e",
            corner_radius=20,
            border_width=2,
            border_color="#d4af37"
        )
        form_frame.grid(row=2, column=0, pady=40, padx=100, sticky="ew")
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Campo usuário
        ctk.CTkLabel(
            form_frame,
            text="👤 Usuário:",
            font=("Arial", 16)
        ).grid(row=0, column=0, pady=(30, 5), padx=40, sticky="w")
        
        self.entry_usuario = ctk.CTkEntry(
            form_frame,
            placeholder_text="Digite seu usuário",
            width=350,
            height=45,
            font=("Arial", 14)
        )
        self.entry_usuario.grid(row=1, column=0, pady=(0, 20), padx=40)
        
        # Campo senha
        ctk.CTkLabel(
            form_frame,
            text="🔒 Senha:",
            font=("Arial", 16)
        ).grid(row=2, column=0, pady=(10, 5), padx=40, sticky="w")
        
        self.entry_senha = ctk.CTkEntry(
            form_frame,
            placeholder_text="Digite sua senha",
            width=350,
            height=45,
            font=("Arial", 14),
            show="•"
        )
        self.entry_senha.grid(row=3, column=0, pady=(0, 30), padx=40)
        
        # Botões
        btn_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_frame.grid(row=4, column=0, pady=(0, 30), padx=40)
        
        btn_login = ctk.CTkButton(
            btn_frame,
            text="🦁 ENTRAR",
            width=170,
            height=50,
            font=("Arial Bold", 16),
            fg_color="#d4af37",
            hover_color="#b8941f",
            text_color="#000",
            command=self._fazer_login
        )
        btn_login.pack(side="left", padx=5)
        
        btn_cadastro = ctk.CTkButton(
            btn_frame,
            text="📝 CADASTRAR",
            width=170,
            height=50,
            font=("Arial Bold", 16),
            command=self._fazer_cadastro
        )
        btn_cadastro.pack(side="left", padx=5)
        
        # Mensagem bônus
        bonus_msg = ctk.CTkLabel(
            self.frame_login,
            text="🎁 Novos jogadores ganham R$100,00 de bônus! 🎁",
            font=("Arial Bold", 16),
            text_color="#44ff44"
        )
        bonus_msg.grid(row=3, column=0, pady=20)
        
        # Bind Enter key
        self.entry_senha.bind("<Return>", lambda e: self._fazer_login())
    
    def _fazer_login(self):
        """Realiza o login do usuário."""
        nome = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        
        if not nome or not senha:
            self._mostrar_erro_login("❌ Preencha todos os campos!")
            return
        
        usuario = self.sistema_auth.login(nome, senha)
        if usuario:
            self.usuario = usuario
            self.maquina.definir_usuario(usuario)
            self.logado = True
            self._login_sucesso()
        else:
            self._mostrar_erro_login("❌ Usuário ou senha incorretos!")
    
    def _fazer_cadastro(self):
        """Realiza o cadastro de novo usuário."""
        nome = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()
        
        if not nome or not senha:
            self._mostrar_erro_login("❌ Preencha todos os campos!")
            return
        
        if self.sistema_auth.cadastrar(nome, senha):
            usuario = self.sistema_auth.login(nome, senha)
            if usuario:
                self.usuario = usuario
                self.maquina.definir_usuario(usuario)
                self.logado = True
                self._login_sucesso()
        else:
            self._mostrar_erro_login("❌ Usuário já existe!")
    
    def _mostrar_erro_login(self, mensagem):
        """Mostra mensagem de erro no login."""
        # Criar label de erro se não existir
        if not hasattr(self, 'label_erro_login'):
            self.label_erro_login = ctk.CTkLabel(
                self.frame_login,
                text="",
                font=("Arial Bold", 14),
                text_color="#ff4444"
            )
            self.label_erro_login.grid(row=4, column=0, pady=10)
        
        self.label_erro_login.configure(text=mensagem)
        self.after(3000, lambda: self.label_erro_login.configure(text=""))
    
    def _login_sucesso(self):
        """Chamado após login bem-sucedido - troca para interface do jogo."""
        # Destruir frame de login
        self.frame_login.destroy()
        
        # Criar interface do jogo
        self._criar_interface_jogo()
    
    def _criar_interface_jogo(self):
        """Cria a interface principal do jogo."""
        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        # === CABEÇALHO ===
        frame_header = ctk.CTkFrame(self, fg_color="#0f3460", corner_radius=0)
        frame_header.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        frame_header.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Título com leões
        label_titulo = ctk.CTkLabel(
            frame_header,
            text="🦁 JOGO DO LEÃOZINHO 🦁",
            font=("Arial Bold", 32),
            text_color="#d4af37"
        )
        label_titulo.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Informações do usuário
        self.label_usuario = ctk.CTkLabel(
            frame_header,
            text="👤 Usuário: ---",
            font=("Arial", 16)
        )
        self.label_usuario.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        
        self.label_saldo = ctk.CTkLabel(
            frame_header,
            text="💰 Saldo: R$ 0.00",
            font=("Arial Bold", 18),
            text_color="#44ff44"
        )
        self.label_saldo.grid(row=1, column=1, pady=10)
        
        # Botões de depositar e sacar
        btn_frame = ctk.CTkFrame(frame_header, fg_color="transparent")
        btn_frame.grid(row=1, column=2, pady=10, padx=20, sticky="e")
        
        btn_depositar = ctk.CTkButton(
            btn_frame,
            text="💵 Depositar",
            width=110,
            height=35,
            font=("Arial", 13),
            command=self._abrir_deposito
        )
        btn_depositar.pack(side="left", padx=5)
        
        btn_sacar = ctk.CTkButton(
            btn_frame,
            text="💰 Sacar",
            width=110,
            height=35,
            font=("Arial", 13),
            fg_color="#44aa44",
            hover_color="#338833",
            command=self._abrir_saque
        )
        btn_sacar.pack(side="left", padx=5)
        
        # === ÁREA DAS ROLETAS ===
        frame_roletas = ctk.CTkFrame(self, fg_color="#1a1a2e")
        frame_roletas.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        frame_roletas.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Container decorativo para as roletas
        frame_container = ctk.CTkFrame(
            frame_roletas,
            fg_color="#16213e",
            corner_radius=20,
            border_width=3,
            border_color="#d4af37"
        )
        frame_container.grid(row=0, column=0, columnspan=3, pady=30, padx=50, sticky="nsew")
        frame_container.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Criar as 3 roletas
        self.roletas = []
        for i in range(3):
            frame_roleta = ctk.CTkFrame(
                frame_container,
                fg_color="#0f3460",
                corner_radius=15,
                width=180,
                height=180
            )
            frame_roleta.grid(row=0, column=i, padx=20, pady=40)
            frame_roleta.grid_propagate(False)
            
            label_roleta = ctk.CTkLabel(
                frame_roleta,
                text="",
                image=self.imagens.get("loading"),
                width=150,
                height=150
            )
            label_roleta.place(relx=0.5, rely=0.5, anchor="center")
            
            self.roletas.append(label_roleta)
        
        # === PAINEL DE CONTROLE ===
        frame_controle = ctk.CTkFrame(self, fg_color="#16213e", corner_radius=15)
        frame_controle.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        frame_controle.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        # Controle de aposta
        label_aposta = ctk.CTkLabel(
            frame_controle,
            text="Valor da Aposta:",
            font=("Arial", 16)
        )
        label_aposta.grid(row=0, column=0, pady=20, padx=10)
        
        btn_menos = ctk.CTkButton(
            frame_controle,
            text="-",
            width=50,
            height=50,
            font=("Arial Bold", 24),
            command=self._diminuir_aposta
        )
        btn_menos.grid(row=0, column=1, pady=20, padx=5)
        
        self.label_valor_aposta = ctk.CTkLabel(
            frame_controle,
            text="R$ 10.00",
            font=("Arial Bold", 24),
            text_color="#d4af37",
            width=120
        )
        self.label_valor_aposta.grid(row=0, column=2, pady=20, padx=10)
        self.valor_aposta = 10.0
        
        btn_mais = ctk.CTkButton(
            frame_controle,
            text="+",
            width=50,
            height=50,
            font=("Arial Bold", 24),
            command=self._aumentar_aposta
        )
        btn_mais.grid(row=0, column=3, pady=20, padx=5)
        
        # Botão de girar (destaque com leão)
        self.btn_girar = ctk.CTkButton(
            frame_controle,
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
        
        # === RODAPÉ ===
        frame_footer = ctk.CTkFrame(self, fg_color="#0f3460", corner_radius=0, height=50)
        frame_footer.grid(row=3, column=0, sticky="ew", padx=0, pady=0)
        frame_footer.grid_columnconfigure((0, 1), weight=1)
        
        btn_premios = ctk.CTkButton(
            frame_footer,
            text="📊 Tabela de Prêmios",
            width=150,
            height=35,
            font=("Arial", 14),
            fg_color="transparent",
            command=self._mostrar_premios
        )
        btn_premios.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        
        btn_sair = ctk.CTkButton(
            frame_footer,
            text="🚪 Sair e Salvar",
            width=150,
            height=35,
            font=("Arial", 14),
            fg_color="#ff4444",
            hover_color="#cc0000",
            command=self._sair
        )
        btn_sair.grid(row=0, column=1, pady=10, padx=20, sticky="e")
    
    def _atualizar_interface(self):
        """Atualiza os elementos da interface com os dados do usuário."""
        if self.usuario:
            self.label_usuario.configure(text=f"👤 Usuário: {self.usuario.nome}")
            self.label_saldo.configure(text=f"💰 Saldo: R$ {self.usuario.get_saldo():.2f}")
    
    def _aumentar_aposta(self):
        """Aumenta o valor da aposta."""
        opcoes = [5.0, 10.0, 20.0, 50.0, 100.0]
        idx = opcoes.index(self.valor_aposta) if self.valor_aposta in opcoes else 0
        if idx < len(opcoes) - 1:
            self.valor_aposta = opcoes[idx + 1]
            self.label_valor_aposta.configure(text=f"R$ {self.valor_aposta:.2f}")
    
    def _diminuir_aposta(self):
        """Diminui o valor da aposta."""
        opcoes = [5.0, 10.0, 20.0, 50.0, 100.0]
        idx = opcoes.index(self.valor_aposta) if self.valor_aposta in opcoes else 0
        if idx > 0:
            self.valor_aposta = opcoes[idx - 1]
            self.label_valor_aposta.configure(text=f"R$ {self.valor_aposta:.2f}")
    
    def _girar_roletas(self):
        """Inicia a animação de giro das roletas."""
        if self.animacao_ativa:
            return
        
        if not self.usuario:
            return
        
        if not self.usuario.pode_apostar(self.valor_aposta):
            self._mostrar_mensagem("❌ Saldo Insuficiente!", "#ff4444")
            return
        
        self.animacao_ativa = True
        self.btn_girar.configure(state="disabled")
        
        # Animar as 3 roletas (mais rápido: 800ms)
        self._animar_giro(duracao=800, intervalo=40)
    
    def _animar_giro(self, duracao, intervalo, tempo_decorrido=0):
        """Animação recursiva do giro."""
        if tempo_decorrido < duracao:
            # Atualizar cada roleta com símbolo COMPLETAMENTE aleatório (incluindo especiais)
            import random
            simbolos_disponiveis = [
                "cereja", "limao", "laranja", "uva", "melancia", 
                "sino", "estrela", "leao", "diamante"
            ]
            
            for roleta in self.roletas:
                simbolo = random.choice(simbolos_disponiveis)
                roleta.configure(image=self.imagens[simbolo])
            
            # Agendar próxima atualização
            self.after(intervalo, lambda: self._animar_giro(duracao, intervalo, tempo_decorrido + intervalo))
        else:
            # Animação terminou - executar jogo real
            self._executar_jogada()
    
    def _executar_jogada(self):
        """Executa a jogada real e mostra o resultado."""
        resultado = self.maquina.jogar(self.valor_aposta)
        
        # Mapear símbolos para nomes de arquivo
        mapa_simbolos = {
            "Cereja": "cereja", "Limão": "limao", "Laranja": "laranja",
            "Uva": "uva", "Melancia": "melancia", "Sino": "sino",
            "Estrela": "estrela", "Leão": "leao", "Diamante": "diamante"
        }
        
        # Mostrar resultado final
        for i, simbolo in enumerate(resultado['simbolos']):
            nome_arquivo = mapa_simbolos.get(simbolo.nome, "loading")
            self.roletas[i].configure(image=self.imagens[nome_arquivo])
        
        # Atualizar interface
        self._atualizar_interface()
        
        # Mostrar mensagem de resultado
        if resultado['ganhou']:
            # Verificar se teve leão
            tem_leao = any(s.nome == "Leão" for s in resultado['simbolos'])
            if tem_leao:
                msg = f"🦁 LEÃO DA SORTE! GANHOU R$ {resultado['premio']:.2f}! 🦁"
            else:
                msg = f"🎉 GANHOU R$ {resultado['premio']:.2f}!"
            cor = "#44ff44"
        else:
            msg = "😢 Não foi desta vez! Tente novamente! 🦁"
            cor = "#ff4444"
        
        self._mostrar_mensagem(msg, cor)
        
        # Salvar progresso
        if self.sistema_auth:
            self.sistema_auth.atualizar_saldo(self.usuario)
        
        # Reabilitar botão
        self.animacao_ativa = False
        self.btn_girar.configure(state="normal")
    
    def _mostrar_mensagem(self, texto, cor="#ffffff"):
        """Mostra uma mensagem temporária na tela."""
        # Criar label temporária
        label_msg = ctk.CTkLabel(
            self,
            text=texto,
            font=("Arial Bold", 28),
            text_color=cor,
            fg_color="#1a1a2e",
            corner_radius=10
        )
        label_msg.place(relx=0.5, rely=0.5, anchor="center")
        
        # Remover após 3 segundos
        self.after(3000, label_msg.destroy)
    
    def _abrir_deposito(self):
        """Abre janela de depósito."""
        if not self.usuario:
            return
        
        dialog = ctk.CTkInputDialog(
            text="Digite o valor do depósito (R$):",
            title="💵 Depositar Créditos"
        )
        
        valor_str = dialog.get_input()
        if valor_str:
            try:
                valor = float(valor_str)
                if self.usuario.depositar(valor):
                    self._atualizar_interface()
                    if self.sistema_auth:
                        self.sistema_auth.atualizar_saldo(self.usuario)
                    self._mostrar_mensagem(f"✅ Depósito de R$ {valor:.2f} realizado!", "#44ff44")
            except ValueError:
                self._mostrar_mensagem("❌ Valor inválido!", "#ff4444")
    
    def _abrir_saque(self):
        """Abre janela de saque."""
        if not self.usuario:
            return
        
        saldo_atual = self.usuario.get_saldo()
        if saldo_atual <= 0:
            self._mostrar_mensagem("❌ Saldo insuficiente para saque!", "#ff4444")
            return
        
        dialog = ctk.CTkInputDialog(
            text=f"Saldo disponível: R$ {saldo_atual:.2f}\nDigite o valor do saque (R$):",
            title="💰 Sacar Créditos"
        )
        
        valor_str = dialog.get_input()
        if valor_str:
            try:
                valor = float(valor_str)
                if valor <= 0:
                    self._mostrar_mensagem("❌ Valor deve ser positivo!", "#ff4444")
                elif valor > saldo_atual:
                    self._mostrar_mensagem("❌ Saldo insuficiente!", "#ff4444")
                elif self.usuario.sacar(valor):
                    self._atualizar_interface()
                    if self.sistema_auth:
                        self.sistema_auth.atualizar_saldo(self.usuario)
                    self._mostrar_mensagem(f"✅ Saque de R$ {valor:.2f} realizado!", "#44ff44")
            except ValueError:
                self._mostrar_mensagem("❌ Valor inválido!", "#ff4444")
    
    def _mostrar_premios(self):
        """Mostra a tabela de prêmios em uma janela."""
        janela = ctk.CTkToplevel(self)
        janela.title("📊 Tabela de Prêmios")
        janela.geometry("600x500")
        janela.resizable(False, False)
        
        texto_premios = """
╔═══════════════════════════════════════════════╗
║      📊 TABELA DE PRÊMIOS 🦁 📊               ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  SÍMBOLOS COMUNS:                             ║
║  🍒 Cereja   - 2x (2 iguais) / 6x (3 iguais) ║
║  🍋 Limão    - 2.5x / 7.5x                    ║
║  🍊 Laranja  - 3x / 9x                        ║
║  🍇 Uva      - 3.5x / 10.5x                   ║
║  🍉 Melancia - 4x / 12x                       ║
║  🔔 Sino     - 5x / 15x                       ║
║  ⭐ Estrela  - 5x / 15x                       ║
║                                               ║
║  SÍMBOLOS ESPECIAIS:                          ║
║  🦁 LEÃO     - 20x / 60x                      ║
║               (Funciona como CORINGA!)        ║
║               MAIS COMUM QUE ANTES! 🦁        ║
║  💎 Diamante - 50x / 150x                     ║
║               (JACKPOT MÁXIMO!)               ║
║                                               ║
╚═══════════════════════════════════════════════╝
        """
        
        label = ctk.CTkLabel(
            janela,
            text=texto_premios,
            font=("Courier New", 13),
            justify="left"
        )
        label.pack(pady=20, padx=20)
        
        btn_fechar = ctk.CTkButton(
            janela,
            text="Fechar",
            width=200,
            height=40,
            command=janela.destroy
        )
        btn_fechar.pack(pady=20)
    
    def _sair(self):
        """Sai do jogo salvando o progresso."""
        if self.usuario and self.sistema_auth:
            self.sistema_auth.atualizar_saldo(self.usuario)
        self.quit()


def main():
    """Função principal que inicia a aplicação."""
    # Criar pasta de dados se não existir
    os.makedirs("dados", exist_ok=True)
    
    # Iniciar aplicação
    app = AplicacaoJogo()
    app.mainloop()


if __name__ == "__main__":
    main()

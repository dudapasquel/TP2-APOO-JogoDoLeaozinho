# 🎨 Documentação da Interface Gráfica

## Visão Geral

A interface gráfica do Jogo do Leãozinho foi desenvolvida com **CustomTkinter**, uma biblioteca moderna que oferece widgets estilizados e uma aparência profissional.

## Estrutura da Interface

### 1. Tela de Login
- **Localização**: `frontend/main_gui.py` - Classe `JanelaLogin`
- **Componentes**:
  - Logo e título do jogo
  - Campo de entrada para usuário
  - Campo de entrada para senha (oculta)
  - Botão "Entrar" (login)
  - Botão "Criar Nova Conta" (cadastro)
  - Label de mensagens (erros/sucessos)

**Funcionalidades**:
- Login de usuários existentes
- Cadastro de novos usuários
- Validação de campos
- Bônus de boas-vindas (R$ 100) para novos usuários

### 2. Tela Principal do Jogo
- **Localização**: `frontend/main_gui.py` - Classe `AplicacaoJogo`

#### Cabeçalho (Header)
- **Título**: "🦁 JOGO DO LEÃOZINHO 🎰"
- **Informações do Usuário**:
  - Nome do usuário logado
  - Saldo atual em destaque (verde)
  - Botão "Depositar" créditos

#### Área das Roletas
- **3 Roletas Animadas**:
  - Cada roleta exibe uma imagem PNG de 150x150 pixels
  - Container decorativo com borda dourada
  - Fundo escuro (#16213e) para contraste

#### Painel de Controle
- **Controle de Aposta**:
  - Botões "-" e "+" para ajustar valor
  - Display do valor atual (dourado)
  - Valores disponíveis: R$ 5, 10, 20, 50, 100
- **Botão "🎰 GIRAR"**:
  - Destaque dourado (#d4af37)
  - Tamanho grande (200x60)
  - Desabilitado durante animação

#### Rodapé (Footer)
- Botão "📊 Tabela de Prêmios"
- Botão "🚪 Sair e Salvar" (vermelho)

## Paleta de Cores

```python
# Cores principais
Fundo Escuro Primário:  #1a1a2e
Fundo Escuro Secundário: #16213e
Azul Escuro (Destaque):  #0f3460
Dourado (Prêmios):       #d4af37
Verde (Ganhou):          #44ff44
Vermelho (Perdeu):       #ff4444
Cinza (Texto):           #888888
```

## Sistema de Animação das Roletas

### Como Funciona

1. **Preparação**:
   ```python
   # Carregar todas as imagens dos símbolos
   self._carregar_imagens()
   ```

2. **Início do Giro**:
   ```python
   def _girar_roletas(self):
       # Validar saldo
       # Desabilitar botão
       # Iniciar animação
       self._animar_giro(duracao=2000, intervalo=50)
   ```

3. **Animação Recursiva**:
   ```python
   def _animar_giro(self, duracao, intervalo, tempo_decorrido=0):
       if tempo_decorrido < duracao:
           # Sortear símbolo aleatório para cada roleta
           # Atualizar imagem
           # Agendar próxima atualização com self.after()
       else:
           # Executar jogada real
           self._executar_jogada()
   ```

4. **Resultado Final**:
   ```python
   def _executar_jogada(self):
       # Executar lógica do backend
       resultado = self.maquina.jogar(self.valor_aposta)
       
       # Mostrar resultado final nas roletas
       # Atualizar saldo
       # Exibir mensagem (ganhou/perdeu)
       # Salvar progresso
       # Reabilitar botão
   ```

### Parâmetros da Animação

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| `duracao` | 2000 ms | Duração total da animação |
| `intervalo` | 50 ms | Tempo entre cada frame |
| `frames` | 40 | Total de frames (2000/50) |

## Mapeamento de Símbolos

```python
# Backend → Frontend
mapa_simbolos = {
    "Cereja": "cereja",
    "Limão": "limao",
    "Laranja": "laranja",
    "Uva": "uva",
    "Melancia": "melancia",
    "Sino": "sino",
    "Estrela": "estrela",
    "Leão": "leao",
    "Diamante": "diamante"
}
```

## Carregamento de Imagens

```python
def _carregar_imagens(self):
    """Carrega todas as imagens dos símbolos."""
    simbolos = ["cereja", "limao", "laranja", "uva", 
                "melancia", "sino", "estrela", "leao", 
                "diamante", "loading"]
    
    for simbolo in simbolos:
        caminho = f"assets/simbolos/{simbolo}.png"
        self.imagens[simbolo] = ctk.CTkImage(
            light_image=Image.open(caminho),
            dark_image=Image.open(caminho),
            size=(150, 150)
        )
```

## Janelas de Diálogo

### Janela de Depósito
```python
def _abrir_deposito(self):
    dialog = ctk.CTkInputDialog(
        text="Digite o valor do depósito (R$):",
        title="💵 Depositar Créditos"
    )
    # Processar valor
    # Atualizar saldo
    # Salvar no JSON
```

### Janela de Tabela de Prêmios
```python
def _mostrar_premios(self):
    janela = ctk.CTkToplevel(self)
    # Exibir tabela formatada
    # Botão fechar
```

### Mensagens Temporárias
```python
def _mostrar_mensagem(self, texto, cor="#ffffff"):
    label_msg = ctk.CTkLabel(...)
    label_msg.place(relx=0.5, rely=0.5, anchor="center")
    self.after(3000, label_msg.destroy)  # Remove após 3s
```

## Integração Backend ↔ Frontend

### Fluxo de Dados

```
Frontend (GUI)
    ↓
    [Botão Girar]
    ↓
    [Validar Saldo]
    ↓
Backend (Lógica)
    ↓
    [Maquina.jogar()]
    ↓
    [Roleta.girar()] × 3
    ↓
    [Verificar Vitória]
    ↓
    [Calcular Prêmio - POLIMORFISMO]
    ↓
Frontend (GUI)
    ↓
    [Atualizar Imagens]
    ↓
    [Mostrar Resultado]
    ↓
    [Atualizar Saldo]
    ↓
Persistência (JSON)
    ↓
    [Salvar no arquivo]
```

## Eventos e Callbacks

### Eventos de Teclado
```python
# Enter no campo de senha = fazer login
self.entry_senha.bind("<Return>", lambda e: self._fazer_login())
```

### Callbacks
```python
# Callback de login bem-sucedido
def _login_sucesso(self, usuario: Usuario, sistema_auth):
    self.usuario = usuario
    self.sistema_auth = sistema_auth
    self.maquina.definir_usuario(usuario)
    self._atualizar_interface()
```

## Responsividade

### Grid System
```python
# Centralizar elementos
self.grid_columnconfigure(0, weight=1)
self.grid_rowconfigure(2, weight=1)

# Distribuir colunas igualmente
frame.grid_columnconfigure((0, 1, 2), weight=1)
```

### Posicionamento
- **Grid**: Para layout estruturado (header, body, footer)
- **Pack**: Para elementos simples (botões em diálogos)
- **Place**: Para elementos sobrepostos (mensagens temporárias)

## Estados dos Componentes

### Botão Girar
```python
# Ativo
self.btn_girar.configure(state="normal")

# Desabilitado (durante animação)
self.btn_girar.configure(state="disabled")
```

### Variável de Controle
```python
self.animacao_ativa = False  # Controla se pode iniciar nova animação
```

## Otimizações

### Pré-carregamento de Imagens
- Todas as imagens são carregadas no `__init__`
- Evita lag durante animação

### Uso do `after()`
- Não bloqueia a interface
- Permite animações suaves
- Melhor que `time.sleep()`

### Lazy Loading
- Diálogos criados sob demanda
- Economiza memória

## Customização Fácil

### Mudar Cores
```python
# Em _criar_interface()
frame_header = ctk.CTkFrame(
    self, 
    fg_color="#NOVA_COR"  # Alterar aqui
)
```

### Mudar Velocidade da Animação
```python
# Em _girar_roletas()
self._animar_giro(
    duracao=3000,    # Mais lento
    intervalo=100    # Frames mais espaçados
)
```

### Adicionar Novos Símbolos
1. Gerar imagem: `gerar_simbolos.py`
2. Adicionar ao backend: `backend/roleta.py`
3. Atualizar mapa: `mapa_simbolos` em `main_gui.py`

## Troubleshooting

### Imagens não aparecem
- Verificar se `assets/simbolos/` existe
- Executar `python gerar_simbolos.py`
- Verificar paths relativos

### Animação travando
- Reduzir `duracao` ou aumentar `intervalo`
- Verificar se há operações pesadas no loop

### Janela não abre
- Verificar se CustomTkinter está instalado
- Verificar se Python tem suporte a Tkinter

## Exemplo Mínimo

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("Teste")
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Olá!", font=("Arial", 24))
label.pack(pady=20)

button = ctk.CTkButton(app, text="Clique", command=lambda: print("Clicou!"))
button.pack(pady=20)

app.mainloop()
```

---

**Desenvolvido com CustomTkinter 5.2.2** 🎨

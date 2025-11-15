# 🦁 Jogo do Leãozinho - Caça-níquel 🎰

## 📋 Sobre o Projeto

Simulador de jogo de caça-níquel desenvolvido em Python para a disciplina de Programação Orientada a Objetos. O projeto implementa um sistema completo de apostas com **interface gráfica moderna (CustomTkinter)**, cadastro de usuários, gerenciamento de saldo e mecânica de jogo com 3 roletas animadas.

## ✨ Características

- 🎨 **Interface Gráfica Moderna** com CustomTkinter
- 🎰 **3 Roletas Animadas** com efeitos visuais
- 💾 **Sistema de Persistência** em JSON
- 🔐 **Login e Cadastro** de usuários
- 💰 **Gerenciamento de Saldo** com validações
- 🦁 **Leão como Coringa** (símbolo especial)
- 💎 **Jackpot de Diamantes** (150x)
- 📊 **Tabela de Prêmios** interativa
- 🎁 **Bônus de Boas-vindas** R$ 100

## 🎯 Tema do Projeto

O projeto é um **simulador de jogo de caça-níquel de 3 roletas**, inspirado em jogos de apostas populares como o "Jogo do Tigrinho". A aplicação simula uma casa de apostas onde o usuário pode:
- ✅ Criar cadastro e fazer login com interface gráfica moderna
- ✅ Gerenciar saldo virtual (adicionar créditos)
- ✅ Fazer apostas e jogar com animações fluidas
- ✅ Visualizar tabela de prêmios interativa
- ✅ Sistema de salvamento automático

## 🖼️ Preview da Interface

### Tela de Login
- Design moderno com tema escuro
- Campos estilizados para usuário e senha
- Botões de login e cadastro
- Validação em tempo real

### Tela Principal
- **Cabeçalho**: Nome do usuário, saldo e botão de depósito
- **Roletas**: 3 roletas animadas com símbolos coloridos
- **Controles**: Botões +/- para ajustar aposta e botão GIRAR em destaque
- **Rodapé**: Acesso à tabela de prêmios e opção de sair

### Animação das Roletas
- Giro suave de 2 segundos
- Troca rápida de símbolos (50ms por frame)
- Resultado final exibido com destaque
- Mensagens de vitória/derrota com cores vibrantes

## 🏗️ Conceitos de POO Implementados

### 1. **Classes**
- **`Usuario`**: Representa o jogador, armazenando nome, senha e saldo
- **`Roleta`**: Representa uma roleta individual com símbolos e método de girar
- **`Simbolo`**: Classe base abstrata para símbolos do jogo
- **`SimboloComum`**: Símbolos regulares (frutas, letras) com multiplicadores menores
- **`SimboloEspecial`**: Símbolos especiais (Leão, Diamante) com multiplicadores maiores
- **`Maquina`**: Classe principal que gerencia 3 roletas e a lógica do jogo
- **`SistemaAutenticacao`**: Gerencia cadastro e login de usuários
- **`JogoDoLeaozinho`**: Controla o fluxo e interface do jogo

### 2. **Herança**
Hierarquia de símbolos implementada:
```
Simbolo (classe abstrata)
    ├── SimboloComum (frutas, letras)
    └── SimboloEspecial (Leão, Diamante)
```

### 3. **Polimorfismo**
A classe `Maquina` calcula prêmios sem precisar saber o tipo específico do símbolo. Simplesmente chama `calcular_premio()` que cada classe implementa de forma diferente.

### 4. **Classe Abstrata**
`Simbolo` é uma classe abstrata (ABC) que define o contrato com o método abstrato `calcular_premio()`. Não pode ser instanciada diretamente.

### 5. **Encapsulamento**
Na classe `Usuario`, o atributo `__saldo` é privado. Só pode ser modificado através dos métodos:
- `depositar(valor)`: Adiciona créditos
- `sacar(valor)`: Remove créditos
- `get_saldo()`: Consulta o saldo

## 📊 Fluxograma do Jogo

```
INÍCIO
   ↓
[Tela Inicial: Boas-vindas]
   ↓
┌──────────────────────┐
│  Menu Principal      │
│  1. Login            │
│  2. Cadastro         │
│  3. Sair             │
└──────────────────────┘
   ↓
[Login/Cadastro]
   ↓
┌──────────────────────┐
│  Menu do Jogo        │
│  1. Jogar            │
│  2. Depositar        │
│  3. Tabela Prêmios   │
│  4. Sair e Salvar    │
└──────────────────────┘
   ↓
[Jogar]
   ↓
[Insere valor aposta]
   ↓
[Valida saldo] ──(Insuficiente)──> [Mensagem Erro]
   ↓ (Válido)
[Debita aposta]
   ↓
[Gira 3 roletas]
   ↓
[Verifica combinação]
   ↓
┌─────────┬─────────┐
│ Ganhou  │ Perdeu  │
│ +Prêmio │ Nada    │
└─────────┴─────────┘
   ↓
[Exibe resultado e saldo]
   ↓
[Volta ao Menu do Jogo]
```

## 🎮 Como Jogar

### Instalação

#### 1. Instalar Python
- **Windows**: Execute `winget install Python.Python.3.12`
- Ou baixe em: https://www.python.org/downloads/
- **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação

#### 2. Instalar Dependências
```bash
# Clone o repositório
git clone https://github.com/dudapasquel/TP2-APOO-JogoDoLeaozinho.git

# Entre no diretório
cd TP2-APOO-JogoDoLeaozinho

# Instale as dependências
python -m pip install -r requirements.txt
```

#### 3. Executar o Jogo
```bash
# Interface Gráfica (CustomTkinter)
python main.py

# Ou interface de linha de comando
python frontend/main_cli.py
```

### Primeiro Acesso
1. Execute o programa
2. Clique em "Criar Nova Conta"
3. Digite usuário e senha
4. Faça login
5. Você receberá R$ 100 de bônus de boas-vindas!
6. Clique em "🎰 GIRAR" e boa sorte!

## 💰 Tabela de Prêmios

### Símbolos Comuns
| Símbolo | Nome | 2 Iguais | 3 Iguais |
|---------|------|----------|----------|
| 🍒 | Cereja | 2x | 6x |
| 🍋 | Limão | 2.5x | 7.5x |
| 🍊 | Laranja | 3x | 9x |
| 🍇 | Uva | 3.5x | 10.5x |
| 🍉 | Melancia | 4x | 12x |
| 🔔 | Sino | 5x | 15x |
| ⭐ | Estrela | 5x | 15x |

### Símbolos Especiais
| Símbolo | Nome | 2 Iguais | 3 Iguais | Especial |
|---------|------|----------|----------|----------|
| 🦁 | Leão | 20x | 60x | Funciona como CORINGA |
| 💎 | Diamante | 50x | 150x | JACKPOT MÁXIMO |

## 📁 Estrutura do Projeto

```
TP2-APOO-JogoDoLeaozinho/
│
├── backend/                    # Lógica de negócio
│   ├── __init__.py
│   ├── simbolo.py             # Classes Simbolo (Abstração + Herança)
│   ├── usuario.py             # Classe Usuario (Encapsulamento)
│   ├── roleta.py              # Classe Roleta
│   ├── maquina.py             # Classe Maquina (Polimorfismo)
│   ├── autenticacao.py        # Sistema de login
│   └── teste.py               # Testes automáticos
│
├── frontend/                   # Interface de usuário
│   ├── __init__.py
│   ├── main_gui.py            # Interface gráfica (CustomTkinter)
│   └── main_cli.py            # Interface de linha de comando
│
├── dados/                      # Persistência de dados
│   └── usuarios.json          # Dados dos usuários (gerado automaticamente)
│
├── assets/                     # Recursos visuais
│   └── simbolos/              # Imagens dos símbolos (PNG)
│       ├── cereja.png
│       ├── limao.png
│       ├── leao.png
│       └── ... (outros símbolos)
│
├── main.py                     # Ponto de entrada principal
├── gerar_simbolos.py          # Script para gerar imagens
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
├── CONCEITOS_POO.md           # Documentação dos conceitos
├── INSTALACAO.md              # Instruções de instalação
└── EXEMPLOS.md                # Exemplos de uso
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **CustomTkinter 5.2.2** - Interface gráfica moderna
- **Pillow 12.0.0** - Manipulação de imagens
- Bibliotecas padrão:
  - `abc` - Classes abstratas
  - `json` - Persistência de dados
  - `random` - Aleatoriedade nas roletas
  - `time` - Animações

### Por que CustomTkinter?

✅ **Estética Moderna**: Interface com cantos arredondados, temas escuro/claro  
✅ **Facilidade de Uso**: Sintaxe similar ao Tkinter padrão  
✅ **Leve e Rápido**: Eficiente para jogos baseados em botões e imagens  
✅ **Animações Simples**: Perfeito para trocar imagens rapidamente (giro das roletas)  
✅ **Multiplataforma**: Funciona em Windows, Mac e Linux

## 👥 Autores

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos.

## 📖 Documentação Adicional

Este projeto conta com documentação completa e detalhada:

- **📘 INICIO_RAPIDO.md** - Guia rápido para começar a jogar em 3 passos
- **📗 CONCEITOS_POO.md** - Explicação detalhada de cada conceito de POO com exemplos
- **📕 INTERFACE_GUI.md** - Documentação técnica da interface CustomTkinter
- **📙 EXEMPLOS.md** - Casos de uso e exemplos práticos do código
- **📔 INSTALACAO.md** - Instruções detalhadas de instalação do Python

## 🎮 Início Rápido

```bash
# 1. Instalar Python
winget install Python.Python.3.12

# 2. Instalar dependências
python -m pip install -r requirements.txt

# 3. Jogar!
python main.py
```

Consulte **INICIO_RAPIDO.md** para instruções detalhadas!

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

---

🎰 **Boa sorte e divirta-se!** 🦁
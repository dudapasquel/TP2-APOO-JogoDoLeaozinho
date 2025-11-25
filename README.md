# 🦁 Jogo do Leãozinho - Caça-níquel 🎰

## 📋 Sobre o Projeto

Simulador de jogo de caça-níquel desenvolvido em Python para a disciplina de Programação Orientada a Objetos. O projeto implementa um sistema completo de apostas com **interface gráfica moderna (CustomTkinter)**, cadastro de usuários, gerenciamento de saldo e mecânica de jogo com 3 roletas animadas.

## ✨ Características

- 🎨 **Interface Gráfica Moderna** com CustomTkinter
- 🎰 **3 Roletas Animadas** com efeitos visuais
- 💾 **Sistema de Persistência** em JSON
- 🔐 **Login e Cadastro** de usuários com validações
- ⚠️ **Tela de Aviso** sobre jogo responsável
- 💰 **Gerenciamento de Saldo** (depósito e saque)
- 💳 **Sistema de Saque PIX** integrado
- ✅ **Validações** de CPF, email e telefone
- 🦁 **Leão como Coringa** (símbolo especial)
- 💎 **Jackpot de Diamantes** (150x)
- 📊 **Tabela de Prêmios** interativa e detalhada
- 📜 **Histórico** de transações e jogadas
- 🎁 **Bônus de Boas-vindas** R$ 10,0000

## 🎯 Tema do Projeto

O projeto é um **simulador de jogo de caça-níquel de 3 roletas**, inspirado em jogos de apostas populares como o "Jogo do Tigrinho". A aplicação simula uma casa de apostas onde o usuário pode:
- ✅ Criar cadastro completo com validações de CPF, email e telefone
- ✅ Fazer login com interface gráfica moderna
- ✅ Ler aviso de jogo responsável antes de começar
- ✅ Gerenciar saldo virtual (depositar e sacar via PIX)
- ✅ Fazer apostas e jogar com animações GIF fluidas
- ✅ Visualizar tabela de prêmios interativa e detalhada
- ✅ Consultar histórico de transações e jogadas
- ✅ Sistema de salvamento automático em JSON

## 🖼️ Preview da Interface

### Tela de Aviso
- Mensagem de jogo responsável obrigatória
- Avisos sobre riscos do jogo
- Confirmação de maioridade
- Design impactante com tema escuro

### Tela de Login
- Design moderno com tema escuro
- Campos estilizados para usuário e senha
- Botões de login e cadastro
- Validação em tempo real
- Mensagem de bônus de R$10,00 para novos usuários

### Tela de Cadastro
- Formulário completo com rolagem
- Campos: nome completo, CPF, email, telefone, usuário e senha
- Validações em tempo real (CPF com verificação de dígitos)
- Design responsivo e moderno

### Tela Principal
- **Cabeçalho**: Nome do usuário, saldo e botões de depósito/saque
- **Roletas**: 3 roletas animadas com símbolos coloridos (imagens PNG)
- **Controles**: Botões +/- para ajustar aposta (R$5 a R$100) e botão GIRAR
- **Rodapé**: Acesso à tabela de prêmios, histórico e opção de sair

### Tela de Saque
- Sistema integrado com PIX
- Validação de chave PIX contra dados cadastrados
- Saldo mínimo: R$50,00
- Proteção contra saques para terceiros
- Confirmação com resumo da operação

### Tela de Histórico
- Abas: Transações e Jogadas
- **Transações**: depósitos, saques, apostas e ganhos
- **Jogadas**: símbolos sorteados, valores e lucro/prejuízo
- Últimas 20 operações de cada tipo
- Interface organizada em tabela

### Animação das Roletas
- Giro suave de 2 segundos
- Troca rápida de símbolos (50ms por frame)
- Resultado final exibido com destaque
- Mensagens de vitória/derrota com cores vibrantes

## 🏗️ Conceitos de POO Implementados

### 1. **Classes**
- **`Usuario`**: Representa o jogador com dados completos (nome, senha, CPF, email, telefone, chave PIX, saldo, históricos)
- **`Roleta`**: Representa uma roleta individual com símbolos e método de girar
- **`Simbolo`**: Classe base abstrata para símbolos do jogo
- **`SimboloComum`**: Símbolos regulares (frutas, letras) com multiplicadores menores
- **`SimboloEspecial`**: Símbolos especiais (Leão, Diamante) com multiplicadores maiores
- **`Maquina`**: Classe principal que gerencia 3 roletas e a lógica do jogo
- **`SistemaAutenticacao`**: Gerencia cadastro, login e persistência de dados em JSON
- **`AplicacaoJogo`**: Controla o fluxo, interface gráfica e todas as telas do jogo

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
```

### Primeiro Acesso
1. Execute o programa
2. Leia e aceite o aviso de jogo responsável
3. Clique em "📝 CADASTRAR"
4. Preencha todos os campos (nome completo, CPF, email, telefone, usuário, senha)
5. O sistema validará CPF, email e telefone automaticamente
6. Após cadastro, você receberá R$ 10,00 de bônus de boas-vindas!
7. Na tela do jogo, ajuste sua aposta (R$5 a R$100)
8. Clique em "🦁 GIRAR 🦁" e boa sorte!
9. Consulte a tabela de prêmios para entender as combinações
10. Para sacar, você precisa ter no mínimo R$50,00

## 💰 Tabela de Prêmios

### Símbolos Comuns
| Símbolo | Nome | Multiplicador Base | 2 Iguais | 3 Iguais |
|---------|------|--------------------|----------|----------|
| 🍒 | Cereja | 2.0x | 2x | 6x |
| 🍋 | Limão | 2.5x | 2.5x | 7.5x |
| 🍊 | Laranja | 3.0x | 3x | 9x |
| 🍇 | Uva | 3.5x | 3.5x | 10.5x |
| 🍉 | Melancia | 4.0x | 4x | 12x |
| 🔔 | Sino | 5.0x | 5x | 15x |
| ⭐ | Estrela | 5.0x | 5x | 15x |

**Regras de Pagamento:**
- 3 símbolos iguais = multiplicador × 3
- 2 símbolos iguais = multiplicador × 1

### Símbolos Especiais
| Símbolo | Nome | Multiplicador Base | 2 Iguais | 3 Iguais | Especial |
|---------|------|--------------------|----------|----------|----------|
| 🦁 | Leão | 20.0x | 20x | 60x | Funciona como CORINGA (combina com qualquer símbolo para bônus 2x) |
| 💎 | Diamante | 50.0x | 50x | 150x | JACKPOT MÁXIMO (símbolo raro) |

## 📁 Estrutura do Projeto

```
TP2-APOO-JogoDoLeaozinho/
│
├── backend/                    # Lógica de negócio
│   ├── __init__.py
│   ├── simbolo.py             # Classe abstrata Simbolo
│   ├── simbolo_comum.py       # Classe SimboloComum (Herança)
│   ├── simbolo_especial.py    # Classe SimboloEspecial (Herança)
│   ├── usuario.py             # Classe Usuario (Encapsulamento)
│   ├── roleta.py              # Classe Roleta
│   ├── maquina.py             # Classe Maquina (Polimorfismo)
│   ├── autenticacao.py        # Sistema de login e persistência
│   ├── diagrama_classes.puml  # Diagrama UML PlantUML
│   └── teste.py               # Testes manuais
│
├── frontend/                   # Interface de usuário
│   └── main_gui.py            # Interface gráfica completa (CustomTkinter)
│
├── dados/                      # Persistência de dados
│   └── usuarios.json          # Dados dos usuários (gerado automaticamente)
│
├── assets/                     # Recursos visuais
│   ├── simbolos/              # Imagens dos símbolos (PNG)
│   │   ├── cereja.png
│   │   ├── limao.png
│   │   ├── laranja.png
│   │   ├── uva.png
│   │   ├── melancia.png
│   │   ├── sino.png
│   │   ├── estrela.png
│   │   ├── leao.png
│   │   ├── diamante.png
│   │   └── loading.png
│   └── roleta_girando.gif     # Animação das roletas (opcional)
│
├── main.py                     # Ponto de entrada principal
├── requirements.txt           # Dependências do projeto
├── DiagramaUML.png            # Diagrama de classes exportado
├── .gitignore                 # Arquivos ignorados pelo Git
└── README.md                  # Este arquivo
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

## 🎮 Início Rápido

```bash
# 1. Instalar Python 3.12+
winget install Python.Python.3.12

# 2. Clonar o repositório
git clone https://github.com/dudapasquel/TP2-APOO-JogoDoLeaozinho.git
cd TP2-APOO-JogoDoLeaozinho

# 3. Instalar dependências
python -m pip install -r requirements.txt

# 4. Jogar!
python main.py
```

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

---

🎰 **Boa sorte e divirta-se!** 🦁
# 🚀 Guia Rápido de Início

## Começar em 3 Passos

### 1️⃣ Instalar Python
```bash
winget install Python.Python.3.12
```

### 2️⃣ Instalar Dependências
```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Jogar!
```bash
python main.py
```

---

## 🎮 Primeira Partida

1. **Criar Conta**
   - Clique em "Criar Nova Conta"
   - Digite usuário (mínimo 3 caracteres)
   - Digite senha (mínimo 4 caracteres)
   - Você ganha R$ 100 de bônus! 🎁

2. **Fazer Login**
   - Digite seu usuário e senha
   - Clique em "Entrar"

3. **Jogar**
   - Use os botões **-** e **+** para ajustar a aposta
   - Clique em **🎰 GIRAR**
   - Veja as roletas girarem!
   - Torça por 3 símbolos iguais 🍀

4. **Depositar Mais**
   - Clique em "💵 Depositar"
   - Digite o valor
   - Continue jogando!

---

## 🎯 Dicas para Ganhar

### Símbolos Mais Valiosos
- 💎 **Diamante** = 50x (150x com 3)
- 🦁 **Leão** = 20x (60x com 3) + **É CORINGA!**
- 🔔 **Sino** = 5x (15x com 3)

### Estratégias
1. **Comece pequeno**: R$ 5 ou R$ 10 por jogada
2. **Leão é seu amigo**: Ele substitui outros símbolos
3. **Gerencie o saldo**: Não aposte tudo de uma vez

---

## 📊 Entendendo os Prêmios

| Combinação | Prêmio |
|------------|--------|
| 3 Diamantes 💎 | **150x** |
| 3 Leões 🦁 | **60x** |
| 3 Sinos 🔔 | **15x** |
| 3 Melancias 🍉 | **12x** |
| 2 Iguais | **2x a 5x** |
| Leão + 2 Iguais | **Prêmio Dobrado** |

---

## 🛠️ Comandos Úteis

### Executar Testes
```bash
cd backend
python teste.py
```

### Recriar Imagens
```bash
python gerar_simbolos.py
```

### Interface CLI (Antiga)
```bash
python frontend/main_cli.py
```

---

## ❓ Problemas Comuns

### "Python não encontrado"
```bash
# Atualizar PATH no terminal atual
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
python --version
```

### "Módulo não encontrado"
```bash
python -m pip install customtkinter pillow
```

### Imagens não aparecem
```bash
python gerar_simbolos.py
```

---

## 📚 Documentação Completa

- **README.md** - Visão geral do projeto
- **CONCEITOS_POO.md** - Explicação detalhada de POO
- **INTERFACE_GUI.md** - Documentação da interface gráfica
- **EXEMPLOS.md** - Exemplos de uso e casos práticos
- **INSTALACAO.md** - Instruções detalhadas de instalação

---

## 🎓 Projeto Acadêmico

Este projeto demonstra:
- ✅ **Classes** e objetos
- ✅ **Herança** (Simbolo → SimboloComum/Especial)
- ✅ **Polimorfismo** (calcular_premio)
- ✅ **Classe Abstrata** (ABC)
- ✅ **Encapsulamento** (saldo privado)

---

**Desenvolvido para Programação Orientada a Objetos** 🎓

**Boa sorte no jogo e no trabalho!** 🍀🦁

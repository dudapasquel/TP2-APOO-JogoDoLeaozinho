# 🎮 Exemplos de Uso do Jogo do Leãozinho

## 1. Exemplo Básico - Primeira Partida

### Passo 1: Iniciar o jogo
```bash
python main.py
```

### Passo 2: Criar conta
```
MENU PRINCIPAL
1. 🔐 Login
2. 📝 Cadastrar novo usuário
3. ❌ Sair

Escolha: 2

Digite seu nome de usuário: jogador1
Digite sua senha: senha123
Confirme sua senha: senha123

✅ Cadastro realizado com sucesso!
```

### Passo 3: Fazer login
```
Escolha: 1

Nome de usuário: jogador1
Senha: senha123

✅ Login realizado com sucesso! Bem-vindo, jogador1!
```

### Passo 4: Depositar créditos
```
MENU DO JOGO
1. 🎰 Jogar
2. 💵 Depositar créditos
3. 📊 Ver tabela de prêmios
4. 🚪 Sair e salvar

Escolha: 2

💰 Saldo atual: R$ 0.00
Digite o valor do depósito: 100

✅ Depósito de R$ 100.00 realizado com sucesso!
💰 Novo saldo: R$ 100.00
```

### Passo 5: Fazer sua primeira aposta
```
Escolha: 1

💰 Saldo disponível: R$ 100.00
Digite o valor da aposta: 10

🎰 Girando as roletas...

╔═══════════════════════════════╗
║    🎰 RESULTADO DO GIRO 🎰    ║
╠═══════════════════════════════╣
║       🍒  |  🍒  |  🍋       ║
╚═══════════════════════════════╝

🎉 PARABÉNS! Você ganhou R$ 20.00!
💰 Saldo atual: R$ 110.00
```

---

## 2. Exemplos de Combinações Vencedoras

### Jackpot de Diamantes (150x)
```
╔═══════════════════════════════╗
║       💎  |  💎  |  💎       ║
╚═══════════════════════════════╝

🎉 JACKPOT! Você ganhou R$ 1500.00!
(Aposta: R$ 10.00 × 50 × 3)
```

### Três Leões (60x)
```
╔═══════════════════════════════╗
║       🦁  |  🦁  |  🦁       ║
╚═══════════════════════════════╝

🎉 GRANDE PRÊMIO! Você ganhou R$ 600.00!
(Aposta: R$ 10.00 × 20 × 3)
```

### Dois Símbolos Iguais (2x a 5x)
```
╔═══════════════════════════════╗
║       🍉  |  🍉  |  🍒       ║
╚═══════════════════════════════╝

🎉 Você ganhou R$ 40.00!
(Aposta: R$ 10.00 × 4)
```

### Leão como Coringa
```
╔═══════════════════════════════╗
║       🍇  |  🦁  |  🍇       ║
╚═══════════════════════════════╝

🎉 Você ganhou R$ 70.00!
(Leão funciona como coringa! Aposta: R$ 10.00 × 3.5 × 2)
```

---

## 3. Exemplo de Código - Usando as Classes

### Criar e Testar Símbolos
```python
from simbolo import SimboloComum, SimboloEspecial

# Criar símbolos
cereja = SimboloComum("Cereja", "🍒", multiplicador=2.0)
leao = SimboloEspecial("Leão", "🦁", multiplicador=20.0, eh_coringa=True)

# Calcular prêmios
aposta = 10.0
premio_cereja = cereja.calcular_premio(aposta)  # 20.0
premio_leao = leao.calcular_premio(aposta)      # 200.0

print(f"Cereja: R${premio_cereja:.2f}")
print(f"Leão: R${premio_leao:.2f}")
```

### Gerenciar Usuário
```python
from usuario import Usuario

# Criar usuário
usuario = Usuario("João", "senha123", saldo_inicial=100.0)

# Verificar saldo
print(f"Saldo: R${usuario.get_saldo():.2f}")  # 100.00

# Depositar
usuario.depositar(50.0)  # Saldo: 150.00

# Tentar sacar
if usuario.sacar(30.0):
    print(f"Saque realizado! Saldo: R${usuario.get_saldo():.2f}")

# Tentar sacar mais do que tem
usuario.sacar(200.0)  # Erro: Saldo insuficiente
```

### Simular uma Jogada
```python
from maquina import Maquina
from usuario import Usuario

# Setup
usuario = Usuario("Teste", "123", saldo_inicial=100.0)
maquina = Maquina()
maquina.definir_usuario(usuario)

# Jogar
resultado = maquina.jogar(10.0)

if resultado['ganhou']:
    print(f"Ganhou R${resultado['premio']:.2f}!")
    print(f"Símbolos: {[s.nome for s in resultado['simbolos']]}")
else:
    print("Não foi desta vez!")

print(f"Saldo: R${usuario.get_saldo():.2f}")
```

---

## 4. Fluxo Completo de Uma Sessão

```
=== INÍCIO ===

1. Abrir o jogo
   → python main.py

2. Cadastrar (primeira vez)
   → Opção 2
   → Nome: maria
   → Senha: maria123

3. Login
   → Opção 1
   → Nome: maria
   → Senha: maria123

4. Depositar
   → Opção 2
   → Valor: 200

5. Ver tabela de prêmios
   → Opção 3
   → (Visualizar multiplicadores)

6. Jogar múltiplas vezes
   → Opção 1 → Apostar 5
   → Opção 1 → Apostar 10
   → Opção 1 → Apostar 20
   → Opção 1 → Apostar 5

7. Sair e salvar
   → Opção 4
   → Progresso salvo automaticamente

8. Retornar depois
   → Login com maria/maria123
   → Saldo mantido! 💰

=== FIM ===
```

---

## 5. Casos de Erro Comuns

### Saldo Insuficiente
```
Digite o valor da aposta: 100

❌ Saldo insuficiente! Saldo atual: R$ 50.00
```

### Senha Incorreta
```
Nome de usuário: joao
Senha: senhaerrada

❌ Erro: Senha incorreta.
```

### Usuário Não Existe
```
Nome de usuário: naoexiste
Senha: 123

❌ Erro: Usuário não encontrado.
```

### Depósito Inválido
```
Digite o valor do depósito: -50

❌ Erro: O valor do depósito deve ser positivo.
```

---

## 6. Estatísticas e Probabilidades

### Probabilidade de Símbolos
- **Símbolos Comuns**: ~90% (3 cópias cada)
- **Símbolos Especiais**: ~10% (1 cópia cada)
  - 🦁 Leão: ~5%
  - 💎 Diamante: ~5%

### Combinações Possíveis
- **3 iguais**: ~5% de chance
- **2 iguais**: ~25% de chance
- **Nenhuma combinação**: ~70% de chance

### Retorno Teórico ao Jogador (RTP)
Aproximadamente 85-90% a longo prazo (típico de caça-níqueis)

---

## 7. Dicas para Jogar

1. **Comece com apostas pequenas** para entender o jogo
2. **Gerencie seu saldo** - não aposte tudo de uma vez
3. **Aproveite quando ganhar** - considere guardar parte dos ganhos
4. **O Leão é seu amigo** - funciona como coringa
5. **Diamante é raro** - mas vale muito a pena!

---

## 8. Comandos Úteis

### Executar o jogo
```bash
python main.py
```

### Executar testes
```bash
python teste.py
```

### Verificar versão do Python
```bash
python --version
```

### Limpar dados de teste
```bash
# Windows PowerShell
Remove-Item usuarios.json
```

---

## 9. Troubleshooting

### Problema: "ModuleNotFoundError"
**Solução:** Certifique-se de estar no diretório correto
```bash
cd "c:\Users\dti-\Desktop\Arquivos\POO\TP2-APOO-JogoDoLeaozinho"
```

### Problema: Arquivo usuarios.json corrompido
**Solução:** Delete o arquivo e recrie os usuários
```bash
Remove-Item usuarios.json
```

### Problema: Animação muito rápida/lenta
**Solução:** Ajuste o `time.sleep()` em `maquina.py` linha 81

---

## 10. Personalizações Possíveis

### Adicionar Novo Símbolo
```python
# Em roleta.py, método _criar_simbolos()
novo_simbolo = SimboloComum("Pêssego", "🍑", multiplicador=4.5)
simbolos.extend([novo_simbolo] * 2)
```

### Mudar Multiplicadores
```python
# Em simbolo.py
leao = SimboloEspecial("Leão", "🦁", multiplicador=30.0)  # Aumenta de 20x para 30x
```

### Adicionar Saldo Bônus no Cadastro
```python
# Em autenticacao.py, método cadastrar()
self._usuarios[nome] = {
    "senha": senha,
    "saldo": 50.0  # Bônus de boas-vindas!
}
```

---

**Divirta-se jogando! 🎰🦁**

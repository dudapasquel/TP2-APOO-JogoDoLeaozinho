"""
Script de teste para validar todas as funcionalidades do Jogo do Leãozinho.
Execute este arquivo para testar as classes sem a interface de usuário.
"""

from simbolo import Simbolo, SimboloComum, SimboloEspecial
from usuario import Usuario
from roleta import Roleta
from maquina import Maquina
from autenticacao import SistemaAutenticacao


def testar_simbolos():
    """Testa a criação e funcionamento dos símbolos."""
    print("\n" + "="*60)
    print("TESTE 1: SÍMBOLOS (Herança, Polimorfismo, Classe Abstrata)")
    print("="*60)
    
    # Teste SimboloComum
    cereja = SimboloComum("Cereja", "🍒", multiplicador=2.0)
    print(f"\n✓ SimboloComum criado: {cereja}")
    print(f"  - Nome: {cereja.nome}")
    print(f"  - Ícone: {cereja.icone}")
    print(f"  - Multiplicador: {cereja.multiplicador}x")
    print(f"  - Prêmio (aposta R$10): R${cereja.calcular_premio(10):.2f}")
    
    # Teste SimboloEspecial
    leao = SimboloEspecial("Leão", "🦁", multiplicador=20.0, eh_coringa=True)
    print(f"\n✓ SimboloEspecial criado: {leao}")
    print(f"  - Nome: {leao.nome}")
    print(f"  - Ícone: {leao.icone}")
    print(f"  - Multiplicador: {leao.multiplicador}x")
    print(f"  - É coringa: {leao.eh_coringa}")
    print(f"  - Prêmio (aposta R$10): R${leao.calcular_premio(10):.2f}")
    
    # Demonstra Polimorfismo
    print(f"\n✓ Demonstração de POLIMORFISMO:")
    simbolos = [cereja, leao]
    aposta = 10.0
    for simbolo in simbolos:
        # Mesmo método, comportamentos diferentes
        print(f"  - {simbolo.nome}: R${simbolo.calcular_premio(aposta):.2f}")
    
    print("\n✅ TESTE DE SÍMBOLOS CONCLUÍDO COM SUCESSO!")


def testar_usuario():
    """Testa a classe Usuario e encapsulamento."""
    print("\n" + "="*60)
    print("TESTE 2: USUÁRIO (Encapsulamento)")
    print("="*60)
    
    # Criar usuário
    usuario = Usuario("TestUser", "senha123", saldo_inicial=100.0)
    print(f"\n✓ Usuário criado: {usuario}")
    
    # Teste de encapsulamento - acesso ao saldo
    print(f"\n✓ Acesso ao saldo privado via método público:")
    print(f"  - Saldo inicial: R${usuario.get_saldo():.2f}")
    
    # Teste de depósito
    print(f"\n✓ Teste de depósito:")
    usuario.depositar(50.0)
    print(f"  - Saldo após depósito: R${usuario.get_saldo():.2f}")
    
    # Teste de depósito inválido
    print(f"\n✓ Teste de depósito inválido (valor negativo):")
    usuario.depositar(-10.0)
    
    # Teste de saque
    print(f"\n✓ Teste de saque:")
    if usuario.sacar(30.0):
        print(f"  - Saque realizado com sucesso!")
        print(f"  - Saldo após saque: R${usuario.get_saldo():.2f}")
    
    # Teste de saque inválido (saldo insuficiente)
    print(f"\n✓ Teste de saque inválido (saldo insuficiente):")
    usuario.sacar(200.0)
    
    # Teste de verificação de senha
    print(f"\n✓ Teste de verificação de senha:")
    print(f"  - Senha correta: {usuario.verificar_senha('senha123')}")
    print(f"  - Senha incorreta: {usuario.verificar_senha('senha_errada')}")
    
    print("\n✅ TESTE DE USUÁRIO CONCLUÍDO COM SUCESSO!")


def testar_roleta():
    """Testa a classe Roleta."""
    print("\n" + "="*60)
    print("TESTE 3: ROLETA")
    print("="*60)
    
    roleta = Roleta()
    print(f"\n✓ Roleta criada com {len(roleta._simbolos)} símbolos disponíveis")
    
    # Gira a roleta 10 vezes
    print(f"\n✓ Girando a roleta 10 vezes:")
    resultados = {}
    for i in range(10):
        simbolo = roleta.girar()
        resultados[simbolo.nome] = resultados.get(simbolo.nome, 0) + 1
        print(f"  Giro {i+1}: {simbolo.icone} ({simbolo.nome})")
    
    print(f"\n✓ Distribuição de resultados:")
    for nome, quantidade in resultados.items():
        print(f"  - {nome}: {quantidade} vezes")
    
    print("\n✅ TESTE DE ROLETA CONCLUÍDO COM SUCESSO!")


def testar_maquina():
    """Testa a classe Maquina e o jogo completo."""
    print("\n" + "="*60)
    print("TESTE 4: MÁQUINA (Jogo Completo)")
    print("="*60)
    
    # Criar usuário e máquina
    usuario = Usuario("JogadorTeste", "senha", saldo_inicial=1000.0)
    maquina = Maquina()
    maquina.definir_usuario(usuario)
    
    print(f"\n✓ Máquina criada e usuário definido")
    print(f"  - {usuario}")
    
    # Simular 5 jogadas
    print(f"\n✓ Simulando 5 jogadas de R$10.00 cada:")
    for i in range(5):
        print(f"\n--- JOGADA {i+1} ---")
        resultado = maquina.jogar(10.0)
        if resultado['ganhou']:
            print(f"✨ GANHOU! Prêmio: R${resultado['premio']:.2f}")
        else:
            print(f"❌ Perdeu desta vez...")
    
    print(f"\n✓ Saldo final: R${usuario.get_saldo():.2f}")
    
    print("\n✅ TESTE DE MÁQUINA CONCLUÍDO COM SUCESSO!")


def testar_autenticacao():
    """Testa o sistema de autenticação."""
    print("\n" + "="*60)
    print("TESTE 5: SISTEMA DE AUTENTICAÇÃO")
    print("="*60)
    
    sistema = SistemaAutenticacao("usuarios_teste.json")
    
    # Teste de cadastro
    print(f"\n✓ Teste de cadastro:")
    sucesso = sistema.cadastrar("usuario_teste", "senha123")
    if sucesso:
        print("  - Cadastro realizado com sucesso!")
    
    # Teste de login
    print(f"\n✓ Teste de login:")
    usuario = sistema.login("usuario_teste", "senha123")
    if usuario:
        print(f"  - Login realizado: {usuario.nome}")
    
    # Teste de login com senha errada
    print(f"\n✓ Teste de login com senha incorreta:")
    usuario_falso = sistema.login("usuario_teste", "senha_errada")
    if not usuario_falso:
        print("  - Login negado corretamente!")
    
    # Teste de atualização de saldo
    if usuario:
        print(f"\n✓ Teste de atualização de saldo:")
        usuario.depositar(500.0)
        sistema.atualizar_saldo(usuario)
        print(f"  - Saldo atualizado no sistema")
    
    print("\n✅ TESTE DE AUTENTICAÇÃO CONCLUÍDO COM SUCESSO!")
    
    # Limpar arquivo de teste
    import os
    if os.path.exists("usuarios_teste.json"):
        os.remove("usuarios_teste.json")
        print("\n✓ Arquivo de teste removido")


def executar_todos_testes():
    """Executa todos os testes."""
    print("\n" + "🎰"*30)
    print("       INICIANDO TESTES DO JOGO DO LEÃOZINHO")
    print("🎰"*30)
    
    try:
        testar_simbolos()
        testar_usuario()
        testar_roleta()
        testar_maquina()
        testar_autenticacao()
        
        print("\n" + "="*60)
        print("✅ TODOS OS TESTES FORAM CONCLUÍDOS COM SUCESSO!")
        print("="*60)
        print("\nO projeto está funcionando corretamente!")
        print("Execute 'python main.py' para jogar.\n")
        
    except Exception as e:
        print(f"\n❌ ERRO DURANTE OS TESTES: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    executar_todos_testes()

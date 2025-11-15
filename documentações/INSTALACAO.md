# 🐍 Instruções de Instalação do Python

## Windows

### Opção 1: Microsoft Store (Recomendado)
1. Abra a Microsoft Store
2. Pesquise por "Python 3.12" (ou versão mais recente)
3. Clique em "Obter" ou "Instalar"
4. Aguarde a instalação

### Opção 2: Site Oficial
1. Acesse: https://www.python.org/downloads/
2. Clique em "Download Python 3.x.x"
3. Execute o instalador baixado
4. **IMPORTANTE**: Marque a opção "Add Python to PATH"
5. Clique em "Install Now"

## Verificando a Instalação

Abra o PowerShell ou Prompt de Comando e execute:

```bash
python --version
```

ou

```bash
python3 --version
```

Você deve ver algo como: `Python 3.12.0`

## Executando o Jogo

Após instalar o Python:

```bash
# Navegue até a pasta do projeto
cd "c:\Users\dti-\Desktop\Arquivos\POO\TP2-APOO-JogoDoLeaozinho"

# Execute o jogo
python main.py
```

## Executando os Testes

Para testar todas as funcionalidades sem a interface:

```bash
python teste.py
```

## Problemas Comuns

### "Python was not found"
- Certifique-se de marcar "Add Python to PATH" durante a instalação
- Reinicie o terminal/PowerShell após instalar
- Tente usar `python3` ao invés de `python`

### Erro de importação
- Certifique-se de estar no diretório correto do projeto
- Todos os arquivos .py devem estar na mesma pasta

## Estrutura de Arquivos Necessária

```
TP2-APOO-JogoDoLeaozinho/
├── main.py           (Principal - execute este)
├── teste.py          (Testes automáticos)
├── simbolo.py        (Classes de símbolos)
├── usuario.py        (Classe de usuário)
├── roleta.py         (Classe da roleta)
├── maquina.py        (Lógica do jogo)
├── autenticacao.py   (Sistema de login)
└── README.md         (Documentação)
```

## Suporte

Se você encontrar problemas:
1. Verifique se o Python está instalado: `python --version`
2. Verifique se está no diretório correto
3. Execute o arquivo de teste: `python teste.py`

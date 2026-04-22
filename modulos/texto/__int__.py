import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def titulo(texto):
    linha = '=' * (len(texto.strip()) + 16)

    print(f'''{linha}
        {texto.strip().title()}
{linha}''')


def linha(qtd=80):
    print('=' * qtd)


def menu():
    print('''[0] - Sair
[1] - Cadastrar funcionário
[2] - Cadastrar cliente
[3] - Cadastrar produto
[4] - Listar funcionários
[5] - Listar clientes
[6] - Listar produtos
[7] - Alterar funcionário
[8] - Alterar cliente
[9] - Alterar produto
[10] - Excluir funcionário
[11] - Excluir cliente
[12] - Excluir produto
[13] - Sair''')

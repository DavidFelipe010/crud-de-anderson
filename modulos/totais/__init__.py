from modulos.texto import titulo, limpar_tela

def total_funcionarios(lst_nome):
    limpar_tela()
    titulo('Total de funcionários')

    print(f'Quantidade de funcionários cadastrados: \033[32m{len(lst_nome)}\033[m')
    input('\nPressione ENTER para continuar...')


def total_clientes(lst_nome):
    limpar_tela()
    titulo('Total de clientes')

    print(f'Quantidade de clientes cadastrados: \033[32m{len(lst_nome)}\033[m')
    input('\nPressione ENTER para continuar...')


def total_produtos(lst_nome):
    limpar_tela()
    titulo('Total de produtos')

    print(f'Quantidade de produtos cadastrados: \033[32m{len(lst_nome)}\033[m')
    input('\nPressione ENTER para continuar...')
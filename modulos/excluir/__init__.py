from modulos.texto import titulo, limpar_tela
from modulos.listar import lista_funcinario, lista_cliente, lista_produto
from modulos.verficadores import verificar_nums_naturais

def excluir_funcionario(lst_nome, lst_cpf, lst_salario):
    limpar_tela()
    titulo('Excluir Funcionário')

    if not lst_nome or not lst_cpf or not lst_salario:
        print(f'\033[31m[ERROR] Não há nenhum funcionário cadastrado atualmente!\033[m')

    else:
        lista_funcinario(lst_nome, lst_cpf, lst_salario)
        ind = verificar_nums_naturais('Qual funcionário você quer excluir? \033[33m[ID]\033[m: ')

        while not 1 <= ind <= len(lst_nome):
            print('\033[31m[ERROR] Não existe nenhum funcionário com esse ID!\033[m\n')
            ind = verificar_nums_naturais('Qual funcionário você quer excluir? \033[33m[ID]\033[m: ')

        limpar_tela()
        certeza = input('Tem certeza que deseja excluir? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().lower()

        while certeza not in ('s','n') or not certeza:
            certeza = input('Tem certeza que deseja excluir? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().lower()

            if certeza:
                certeza = certeza[0]

        limpar_tela()
        if certeza == 's':
            limpar_tela()
            print(f'\033[32mFuncionário com o NOME de "\033[1;34m{lst_nome[ind - 1].title()}"\033[32m excluido com sucesso!\033[m')
            lst_nome.pop(ind - 1)
            lst_cpf.pop(ind - 1)
            lst_salario.pop(ind - 1)

        else:
            print('\033[31mOperação cancelada!\033[m')

        input('\nPressione ENTER para continuar...')


def excluir_cliente(lst_nome, lst_cpf, lst_endereco):
    limpar_tela()
    titulo('Excluir Cliente')

    if not lst_nome or not lst_cpf or not lst_endereco:
        print(f'\033[31m[ERROR] Não há nenhum cliente cadastrado atualmente!\033[m')

    else:
        lista_cliente(lst_nome, lst_cpf, lst_endereco)
        ind = verificar_nums_naturais('Qual cliente você quer excluir? \033[33m[ID]\033[m: ')

        while not 1 <= ind <= len(lst_nome):
            print('\033[31m[ERROR] Não existe nenhum cliente com esse ID!\033[m\n')
            ind = verificar_nums_naturais('Qual cliente você quer excluir? \033[33m[ID]\033[m: ')

        limpar_tela()
        certeza = input('Tem certeza que deseja excluir? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().lower()

        while certeza not in ('s','n') or not certeza:
            certeza = input('Tem certeza que deseja excluir? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().lower()

            if certeza:
                certeza = certeza[0]

        limpar_tela()
        if certeza == 's':
            limpar_tela()
            print(f'\033[32mCliente com o NOME de "\033[1;34m{lst_nome[ind - 1].title()}"\033[32m excluido com sucesso!\033[m')
            lst_nome.pop(ind - 1)
            lst_cpf.pop(ind - 1)
            lst_endereco.pop(ind - 1)

        else:
            print('\033[31mOperação cancelada!\033[m')

        input('\nPressione ENTER para continuar...')


def excluir_produto(lst_nome, lst_preco):
    limpar_tela()
    titulo('Excluir Produto')

    if not lst_nome or not lst_preco:
        print(f'\033[31m[ERROR] Não há nenhum produto cadastrado atualmente!\033[m')

    else:
        lista_produto(lst_nome, lst_preco)
        ind = verificar_nums_naturais('Qual produto você quer excluir? \033[33m[ID]\033[m: ')

        while not 1 <= ind <= len(lst_nome):
            print('\033[31m[ERROR] Não existe nenhum produto com esse ID!\033[m\n')
            ind = verificar_nums_naturais('Qual produto você quer excluir? \033[33m[ID]\033[m: ')

        limpar_tela()
        certeza = input('Tem certeza que deseja excluir? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().lower()

        while certeza not in ('s','n') or not certeza:
            certeza = input('Tem certeza que deseja excluir? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().lower()

            if certeza:
                certeza = certeza[0]

        limpar_tela()
        if certeza == 's':
            limpar_tela()
            print(f'\033[32mProduto com o NOME de "\033[1;34m{lst_nome[ind - 1].title()}"\033[32m excluido com sucesso!\033[m')
            lst_nome.pop(ind - 1)
            lst_preco.pop(ind - 1)

        else:
            print('\033[31mOperação cancelada!\033[m')

        input('\nPressione ENTER para continuar...')
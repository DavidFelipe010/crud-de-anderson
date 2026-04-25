from modulos.texto import titulo, limpar_tela, linha
from modulos.listar import lista_funcinario, lista_cliente, lista_produto
from modulos.verficadores import verificar_nums_naturais, verificar_nome, verificar_cpf, verificar_salario, verificar_endereco, verificar_preco_produto






def menu_alterar_funcionarios(lst_nome, lst_cpf, lst_salario):
    limpar_tela()
    titulo("Alterar dados de funcionarios")
    lista_funcinario(lst_nome, lst_cpf, lst_salario)

    while True:
        opcao = verificar_nums_naturais('\nAltera:  nome(1) | CPF(2) | endereco(3) | Sair(0): ')
        
        match opcao:
            case 0:
                input('\nPressione ENTER para continuar...')
                return True
            case 1:
                if alterar_nome_funcionarios(lst_nome, lst_cpf, lst_salario):
                    return True 
            case 2:
                if alterar_cpf_funcionarios(lst_nome, lst_cpf, lst_salario):
                    return True
            case 3:
                if alterar_salario_funcionarios(lst_nome, lst_cpf, lst_salario):
                    return True 
            case _:
                print('\033[31m[ERROR] Escolha uma opção válida (1-3).\033[m')
                input('\nPressione ENTER para continuar...')


def alterar_nome_funcionarios(lst_nome, lst_cpf, lst_salario):
    while True:
        
        limpar_tela()
        titulo("Alterar dados de funcionarios")

        print("Alterar Nome".title().center(50))
        linha()

        lista_funcinario(lst_nome, lst_cpf, lst_salario)
        
        id_escolhido = verificar_nums_naturais('\nDigite o ID (0=cancelar): ')
        
        if id_escolhido == 0:
            print("Cancelado")
            input("\nPressione ENTER para continuar...")
            return False
        
        if 1 <= id_escolhido <= len(lst_nome):
            indice = id_escolhido - 1
            novo_nome = verificar_nome('Digite o novo nome: ')
            lst_nome[indice] = novo_nome

            print(f'\033[32m[Sucesso] Nome alterado: {novo_nome}\033[m')
            input('\nPressione ENTER para continuar...')
            return True
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('Pressione ENTER para tentar novamente...')
 

def alterar_cpf_funcionarios(lst_nome, lst_cpf, lst_salario):
    while True:

        limpar_tela()
        titulo("alterar dados de funcionarios")

        print('alterar CPF'.title().center(50))
        linha()

        lista_funcinario(lst_nome, lst_cpf, lst_salario)

        id_escolhido = verificar_nums_naturais("\nDigite o ID (0=cancelar): ")

        if id_escolhido == 0:
            print("Cancelado")
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_cpf):
            indice = id_escolhido - 1
            novo_cpf = verificar_cpf("Digite o novo CPF: ")
            lst_cpf[indice] = novo_cpf

            print(f'\033[32m[Sucesso] CPF alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')


def alterar_salario_funcionarios(lst_nome, lst_cpf, lst_salario):
    while True:
        limpar_tela()
        titulo('alterar dados dos funcionarios')

        print('alterar salario'.title().center(50))
        linha()

        lista_funcinario(lst_nome, lst_cpf, lst_salario)

        id_escolhido = verificar_nums_naturais('Digite o ID (0=cancelar): ')
        if id_escolhido == 0:
            print('Cancelado')
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_salario):
            indice = id_escolhido - 1
            novo_salario = verificar_salario('Digite o novo salario: ')
            lst_salario[indice] = novo_salario

            print(f'\033[32m[Sucesso] endereco alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')





def menu_alterar_cliente(lst_nome, lst_cpf, lst_endereco):
    limpar_tela()
    titulo("Alterar dados de cliente")
    lista_cliente(lst_nome, lst_cpf, lst_endereco)

    while True:
        opcao = verificar_nums_naturais('\nAltera:  nome(1) | CPF(2) | endereco(3) | Sair(0): ')
        
        match opcao:
            case 0:
                input('\nPressione ENTER para continuar...')
                return True
            case 1:
                if alterar_nome_clientes(lst_nome, lst_cpf, lst_endereco):
                    return True 
            case 2:
                if alterar_cpf_clientes(lst_nome, lst_cpf, lst_endereco):
                    return True
            case 3:
                if alterar_endereco_clientes(lst_nome, lst_cpf, lst_endereco):
                    return True 
            case _:
                print('\033[31m[ERROR] Escolha uma opção válida (1-3).\033[m')
                input('\nPressione ENTER para continuar...')


def alterar_nome_clientes(lst_nome, lst_cpf, lst_endereco):
    while True:

        limpar_tela()
        titulo("alterar dados de funcionarios")

        print('alterar nome'.title().center(50))
        linha()

        lista_cliente(lst_nome, lst_cpf, lst_endereco)

        id_escolhido = verificar_nums_naturais("\nDigite o ID (0=cancelar): ")

        if id_escolhido == 0:
            print("Cancelado")
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_cpf):
            indice = id_escolhido - 1
            novo_nome = verificar_nome("Digite o novo Nome: ")
            lst_nome[indice] = novo_nome

            print(f'\033[32m[Sucesso] Nome alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')


def alterar_cpf_clientes(lst_nome, lst_cpf, lst_endereco):
    while True:

        limpar_tela()
        titulo("alterar dados de clientes")

        print('alterar CPF'.title().center(50))
        linha()

        lista_funcinario(lst_nome, lst_cpf, lst_endereco)

        id_escolhido = verificar_nums_naturais("\nDigite o ID (0=cancelar): ")

        if id_escolhido == 0:
            print("Cancelado")
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_cpf):
            indice = id_escolhido - 1
            novo_cpf = verificar_cpf("Digite o novo CPF: ")
            lst_cpf[indice] = novo_cpf

            print(f'\033[32m[Sucesso] CPF alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')


def alterar_endereco_clientes(lst_nome, lst_cpf, lst_endereco):
    while True:

        limpar_tela()
        titulo("alterar dados de clientes")

        print('alterar endereço'.title().center(50))
        linha()

        lista_cliente(lst_nome, lst_cpf, lst_endereco)

        id_escolhido = verificar_nums_naturais("\nDigite o ID (0=cancelar): ")

        if id_escolhido == 0:
            print("Cancelado")
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_endereco):
            indice = id_escolhido - 1
            novo_endereco = verificar_endereco("Digite o novo endereço: ")
            lst_cpf[indice] = novo_endereco

            print(f'\033[32m[Sucesso] Endereço alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')





def menu_alterar_produtos(lst_nome, lst_preco):

    limpar_tela()
    titulo("Alterar dados de produtos")
    lista_funcinario(lst_nome, lst_preco)

    while True:
        opcao = verificar_nums_naturais('\nAltera: Nome(1) | Preço(2) | Sair(0): ')
        
        match opcao:
            case 0:
                input('\nPressione ENTER para continuar...')
                return True
            case 1:
                if alterar_nome_produtos(lst_nome, lst_preco):
                    return True 
            case 2:
                if alterar_preco_produtos(lst_nome, lst_preco):
                    return True
            case _:
                print('\033[31m[ERROR] Escolha uma opção válida (1-3).\033[m')
                input('\nPressione ENTER para continuar...')


def alterar_nome_produtos(lst_nome, lst_preco):
    while True:

        limpar_tela()
        titulo("alterar dados de produtos")

        print('alterar nome'.title().center(50))
        linha()

        lista_produto(lst_nome, lst_preco)

        id_escolhido = verificar_nums_naturais("\nDigite o ID (0=cancelar): ")

        if id_escolhido == 0:
            print("Cancelado")
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_nome):
            indice = id_escolhido - 1
            novo_nome = verificar_nome("Digite o novo Nome: ")
            lst_nome[indice] = novo_nome

            print(f'\033[32m[Sucesso] Nome alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')


def alterar_preco_produtos(lst_nome, lst_preco):
    while True:

        limpar_tela()
        titulo("alterar dados de produtos")

        print('alterar preço'.title().center(50))
        linha()

        lista_produto(lst_nome, lst_preco)

        id_escolhido = verificar_nums_naturais("\nDigite o ID (0=cancelar): ")

        if id_escolhido == 0:
            print("Cancelado")
            input('\nPressione ENTER para continuar...')
            return False
        
        if 1 <= id_escolhido <= len(lst_preco):
            indice = id_escolhido - 1
            novo_preco = verificar_preco_produto("Digite o novo preço: ")
            lst_preco[indice] = novo_preco

            print(f'\033[32m[Sucesso] Nome alterado\033[m')
            return True
        
        else:
            print(f'\033[31m[ERROR] ID {id_escolhido} não existe!\033[m')
            input('\nPressione ENTER para continuar...')
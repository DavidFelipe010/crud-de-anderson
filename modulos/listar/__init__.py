from modulos.texto import linha, limpar_tela, titulo, formatar_cpf, formatar_endereco

def lista_funcinario(lst_nome, lst_cpf, lst_enderoco):

    linha(60)
    print(f"{'ID':<5} {'Nome':<16} {'CPF':<16} {'Salario':<12}")
    linha(60)

    for id, (nome, cpf, salario) in enumerate(zip(lst_nome, lst_cpf, lst_enderoco), 1):
        print(f"{f'[{id}]':<5} {nome.title():<16} {formatar_cpf(cpf):<16} R${salario:<12,.2f}")

 
def listar_funcionario(lst_nome, lst_cpf, lst_enderoco):

    limpar_tela()
    titulo("Listar Funcionario")
    
    if not lst_nome or not lst_cpf or not lst_enderoco:
        print('\033[31m[ERROR] Não há funcionarios cadastrados para listar.\033[m\n')
        
    else:        
         lista_funcinario(lst_nome, lst_cpf, lst_enderoco)

    input("\nPressione ENTER para continuar...")


def lista_cliente(lst_nome, lst_cpf, lst_endereco):

    linha(100)
    print(f"{'ID':<5} {'Nome':<16} {'CPF':<16} {'Endereço':<12}")
    linha(100)

    for id, (nome, cpf, endereco) in enumerate(zip(lst_nome, lst_cpf, lst_endereco), 1):
        print(f"{f'[{id}]':<5} {nome.title():<16} {formatar_cpf(cpf):<16} {formatar_endereco(endereco):<12}")


def listar_cliente(lst_nome, lst_cpf, lst_enderoco):

    limpar_tela()
    titulo("Listar Cliente")
    
    if not lst_nome or not lst_cpf or not lst_enderoco:
        print('\033[31m[ERROR] Não há clientes cadastrados para listar.\033[m\n')
        
    else:        
         lista_cliente(lst_nome, lst_cpf, lst_enderoco)

    input("\nPressione ENTER para continuar...")


def lista_produto(lst_nome, lst_preco):

    linha(50)
    print(f"{'ID':<5} {'Nome':<22} {'Preço':<16}")
    linha(50)

    for id, (nome, preco) in enumerate(zip(lst_nome, lst_preco), 1):
        print(f"{f'[{id}]':<5} {nome.title():<22} R${preco:<16,.2f}")


def listar_produto(lst_nome, lst_preco):

    limpar_tela()
    titulo("Listar Produtos")
    
    if not lst_nome or not lst_preco:
        print('\033[31m[ERROR] Não há produtos cadastrados para listar.\033[m\n')
        
    else:        
         lista_produto(lst_nome, lst_preco)

    input("\nPressione ENTER para continuar...")
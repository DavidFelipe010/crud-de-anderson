from modulos.verficadores import verificar_nome, verificar_cpf, verificar_salario, verificar_preco_produto, verificar_endereco
from modulos.texto import limpar_tela, titulo

def cadastrar_funcionario(lst_nome, lst_cpf, lst_salario):
    limpar_tela()
    titulo('Cadastro de Funcionário')
    
    nome = verificar_nome('Digite o nome do funcionário (primeiro e ultimo nome): ')
    cpf = verificar_cpf('Digite o CPF do funcionário (apenas números): ')
    salario = verificar_salario('Digite o salário do funcionário: ')

    lst_nome.append(nome)
    lst_cpf.append(cpf)
    lst_salario.append(salario)


def cadastrar_cliente(lst_nome, lst_cpf, lst_endereco):
    limpar_tela()
    titulo('Cadastro de Cliente')

    nome = verificar_nome('Digite o nome do cliente (primeiro e ultimo nome): ')
    cpf = verificar_cpf('Digite o CPF do cliente (apenas números): ')
    endereco = verificar_endereco()

    lst_nome.append(nome)
    lst_cpf.append(cpf)
    lst_endereco.append(endereco)


def cadastrar_produto(lst_nome, lst_preco):
    limpar_tela()
    titulo('Cadastro de Produto')

    nome = verificar_nome('Digite o nome do produto: ')
    preco = verificar_preco_produto('Digite o preço do produto: ')

    lst_nome.append(nome)
    lst_preco.append(preco)

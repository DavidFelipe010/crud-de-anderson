from modulos.cadastrar import cadastrar_funcionario
from modulos.excluir import excluir_funcionario

def main():
   nome_funcionarios = []
   cpf_funcionarios = []
   salario_funcionarios = []
   
   nome_clientes = []
   cpf_clientes = []
   endereco_clientes = []

   nome_produtos = []
   preco_produto = []

   cadastrar_funcionario(nome_funcionarios,cpf_funcionarios, salario_funcionarios)
   excluir_funcionario(nome_funcionarios,cpf_funcionarios, salario_funcionarios)

if __name__ == '__main__':
    main()
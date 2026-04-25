from modulos.cadastrar import cadastrar_cliente, cadastrar_funcionario, cadastrar_produto
from modulos.listar import listar_funcionario, listar_cliente, listar_produto
def main():
   nome = []
   cpf = []
   salario = []
   
   nome_cliente = []
   cpf_cliente = []
   endereco = []

   nome_produto = []
   preco_produto = []

   cadastrar_produto(nome_produto, preco_produto)
   listar_produto(nome_produto, preco_produto)
if __name__ == '__main__':
    main()
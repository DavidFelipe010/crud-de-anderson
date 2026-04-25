from modulos.cadastrar import cadastrar_funcionario, cadastrar_cliente, cadastrar_produto
from modulos.listar import listar_funcionario, listar_cliente, listar_produto
from modulos.alterar import menu_alterar_funcionarios, menu_alterar_cliente, menu_alterar_produtos
from modulos.excluir import excluir_funcionario, excluir_cliente, excluir_produto
from modulos.totais import total_funcionarios, total_clientes, total_produtos
from modulos.verficadores import verificar_nums_naturais
from modulos.texto import menu, limpar_tela, linha

def main():
   nome_funcionarios = []
   cpf_funcionarios = []
   salario_funcionarios = []
   
   nome_clientes = []
   cpf_clientes = []
   endereco_clientes = []

   nome_produtos = []
   preco_produtos = []

   while True:
      limpar_tela()
      txt = 'Menu de Opções'

      print(f'''{"=" * (len(txt) + 16):^100}
      {txt:^88}
{"=" * (len(txt) + 16):^100}''')

      linha(100)
      menu()
      linha(100)

      esc = verificar_nums_naturais('Sua escolha: ')

      match esc:
         case 0:
            limpar_tela()
            print('\033[32mObrigado por utilizar nosso CRUD! Volte sempre!\033[m')
            break

         case 1:
            cadastrar_funcionario(nome_funcionarios, cpf_funcionarios, salario_funcionarios)

         case 2:
            listar_funcionario(nome_funcionarios, cpf_funcionarios, salario_funcionarios)

         case 3:
            menu_alterar_funcionarios(nome_funcionarios, cpf_funcionarios, salario_funcionarios)

         case 4:
            excluir_funcionario(nome_funcionarios, cpf_funcionarios, salario_funcionarios)

         case 5:
            cadastrar_cliente(nome_clientes, cpf_clientes, endereco_clientes)

         case 6:
            listar_cliente(nome_clientes, cpf_clientes, endereco_clientes)

         case 7:
            menu_alterar_cliente(nome_clientes, cpf_clientes, endereco_clientes)

         case 8:
            excluir_cliente(nome_clientes, cpf_clientes, endereco_clientes)

         case 9:
            cadastrar_produto(nome_produtos, preco_produtos)

         case 10:
            listar_produto(nome_produtos, preco_produtos)

         case 11:
            menu_alterar_produtos(nome_produtos, preco_produtos)

         case 12:
            excluir_produto(nome_produtos, preco_produtos)

         case 13:
            total_funcionarios(nome_funcionarios)

         case 14:
            total_clientes(nome_funcionarios)

         case 15:
            total_produtos(nome_produtos)

         case _:
            limpar_tela()
            print(f'\033[31m[ERROR] Escolha inexistente! Escolha um valor entre \033[33m[0-15]\033[31m!\033[m')
            input('\nPressione ENTER para continuar...')


if __name__ == '__main__':
    main()
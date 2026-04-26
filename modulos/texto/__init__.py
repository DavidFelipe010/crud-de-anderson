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
    print(f'''\033[31m[0] - Sair\033[m                                          \033[32m[1] - Cadastrar funcionário
[2] - Listar funcionários                           [3] - Alterar funcionário
[4] - Excluir funcionário\033[m                           \033[33m[5] - Cadastrar cliente     
[6] - Listar clientes                               [7] - Alterar cliente       
[8] - Excluir cliente\033[m                               \033[34m[9] - Cadastrar produtos       
[10] - Listar produtos                              [11] - Alterar produto
[12] - Excluir produto\033[m                      
{"=" * 100}
\033[32m[13] - Ver o total de funcionários cadastrados\033[m    \033[33m[14] - Ver o total de clientes cadastrados\033[m  
\033[34m[15] - Ver o total de produtos cadastrados\033[m''')

def formatar_cpf(cpf: str) -> str:
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def formatar_endereco(endereco: list) -> str:
    numero, rua, bairro, cidade, estado, complemento = endereco
    if not complemento:
        return f'Rua {rua.title()}, nº {numero}, Bairro {bairro.title()}, {cidade.title()} – {estado.title()}'
    
    return f'Rua {rua.title()}, nº {numero}, Bairro {bairro.title()}, {cidade.title()} – {estado.title()}, {complemento}'
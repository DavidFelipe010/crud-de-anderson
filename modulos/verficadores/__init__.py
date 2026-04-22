def verificar_int(txt: str) -> int:
    while True:
        label = input(txt).strip()
        
        try:
            num = int(label)
            return num
        
        except (ValueError, TypeError):
            print('\033[31m[ERROR] Entrada deve ser um número inteiro válido.\033[m\n')


def verificar_nums_naturais(txt: str) -> int:
    while True:
        label = input(txt).strip()
        
        try:
            num = int(label)
            
            if num < 0:
                print('\033[31m[ERROR] Entrada deve ser um número inteiro positivo.\033[m\n')
                continue
            
            return num
        
        except (ValueError, TypeError):
            print('\033[31m[ERROR] Entrada deve ser um número inteiro válido.\033[m\n')


def verificar_nome(txt: str) -> str:
    label = input(txt).strip().lower()

    while len(label) < 3 or (c for c in label if not (c.isalpha() or c.isspace())):
        print('\033[31m[ERROR] O nome deve conter pelo menos 3 caracteres.\033[m\n')
        label = input(txt).strip().lower()
    
    return label


def verificar_salario(txt: str) -> float:
    while True:
        label = input(txt).strip().replace(',', '.')
        try:
            salario = float(label)
            
            if salario < 0:
                print('\033[31m[ERROR] O salário deve ser um valor positivo.\033[m\n')
                continue
            
            return salario
        
        except (ValueError, TypeError):
            print('\033[31m[ERROR] Salário deve ser um número válido.\033[m\n')


def verificar_cpf(txt: str) -> str:
    label = input(txt).strip()

    while len(label) != 11 or not label.isdigit():
        print('\033[31m[ERROR] CPF deve conter 11 dígitos numéricos.\033[m\n')
        label = input(txt).strip()
    
    return label


def verificar_preco_produto(txt: str) -> float:
    while True:
        label = input(txt).strip().replace(',', '.')
        try:
            salario = float(label)
            
            if salario < 0:
                print('\033[31m[ERROR] O salário deve ser um valor positivo.\033[m\n')
                continue
            
            return salario
        
        except (ValueError, TypeError):
            print('\033[31m[ERROR] Salário deve ser um número válido.\033[m\n')


def verificar_endereco() -> list:
    num = verificar_nums_naturais('Número do endereço: ')
    rua = input('Rua: ').strip().lower()
    bairro = input('Bairro: ').strip().lower()
    cidade = input('Cidade: ').strip().lower()
    estado = input('Estado: ').strip().lower()
    complemento = input('Complemento (opcional): ').strip().lower()

    endereco = [num, rua, bairro, cidade, estado, complemento]

    return endereco
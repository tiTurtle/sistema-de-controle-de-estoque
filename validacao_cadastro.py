""" Validação dos campos de entrada da função cadastro_produtos() """

def validar_codigo_cadastro(estoque):
    while True:
        try:
            codigo = int(input("Insira o código do produto:\n"))
            if any(produto["codigo"] == codigo for produto in estoque):
                print("Produto já cadastrado")
            else:
                return codigo
        except ValueError:
            print("Digite somente números inteiros")

def validar_quantidade():
    while True:
        try:
            quantidade = int(input("Insira a quantidade de produtos em estoque:\n"))
            if quantidade >= 0:
                return quantidade
            else:
                print("O estoque não pode ser negativo")
        except:
            print("Digite somente quantidades inteiras, ou nulas, positivas")

def validar_custo():
    while True:
        try:
            custo = float(input("Digite o custo do produto:\n"))
            if custo > 0:
                return custo
            else:
                print("O custo não pode ser negativo ou igual a zero")
        except:
            print("Digite somente números")

def validar_preco():
    while True:
        try:
            preco = float(input("Digite o preço do produto:\n"))
            if preco > 0:
                return preco
            else:
                print("O preco não pode ser negativo ou igual a zero")
        except:
            print("Digite somente números")

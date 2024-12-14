from tratar_dados_estoque import *

def achar_produtos():

    global estoque

    while True:
        try:
            index = int(input("Digite o código do produto:\n"))
            produto_encontrado = False

            for i in estoque:
                if i["codigo"] == index:
                    produto_encontrado = True
                    return i

            if not produto_encontrado:
                print("Produto não encontrado")

        except ValueError:
            print("Erro: Digite apenas números para o código do produto.")

def validacao_pergunta():
    while True:
        pergunta = input("Deseja repetir a operação? (s/n)").lower()
        if pergunta in ["s", "n"]:
            return pergunta
        else:
            print("Digite somente \'s\' ou \'n\' ")


#Valida a nova quantidade na função atualizar_quantidade()
def validar_nova_quantidade():
    while True:
        try:
            quantidade = int(input("Digite o quanto você quer somar/subtrair: "))
            if quantidade <= 0:
                print("Insira um número inteiro maior que 0")
            else:
                return quantidade
        except ValueError:
            print("Erro: Digite apenas números inteiros para o código do produto.")


#FUnção auxiliar para o usuário escolher soma ou subtração na função atualizar_quantidade()
def somar_ou_subtrair():
    while True:
        try:
            operacao = int(input("Deseja [1] - somar\n[2] - subtrair\n"))
            if operacao not in [1, 2]:
                print("Escolha 1 ou 2")
            else:
                return operacao
        except ValueError:
            print("Insira somente números (1 ou 2)")

#FUnção auxiliar para valiar o novo preço do produto na função atualizar_quantidade()
def validar_preco_novo():
    while True:
        try:
            novoPreco = float(input("Digite o novo preço do produto: "))
            if novoPreco <= 0:
                print("O novo preço tem que ser maior que zero")
            else:
                return novoPreco
        except ValueError:
            print("Erro: Digite apenas números reais positivos maiores que 0.")

# Valida as opções da função menu()
def validar_opcao_menu():
    while True:
        try:
            opcao = int(input("Insira uma opcão:\n"))
            if opcao in range (13): # [0,1,2,3,4,5,6,7,8,9,10,11]
                return opcao
            else:
                print("Digite um número equivalente ao número de alguma opção")
        except ValueError:
            print("Insira somente números inteiros")

#Função criada exclusivamente para printar a função buscar_produto()
def printar(parametro):
    print(parametro)
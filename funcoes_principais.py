from tratar_dados_estoque import *
from validacao_cadastro import *
from funcoes_auxiliares import *

flag_baixa_quantidade = 10


#Cadastro de novos produtos
def cadastro_produtos ():
    print("Você optou por registar um produto no estoque\n")
    global estoque

    while True:
        
        descricao = input("Insira a descrição do produto:\n")
        codigo = validar_codigo_cadastro(estoque)
        quantidade = validar_quantidade()
        
        while True:
            custoItem = validar_custo()
            precoVenda = validar_preco()

            if custoItem > precoVenda:
                print("O custo não pode ser maior que o preço. Tente novamente.")
                continue
            break

        estoque.append({'descricao': descricao, 'codigo': codigo, 'quantidade': quantidade, 'custoItem': custoItem, 'precoVenda': precoVenda})
        print(estoque)

        pergunta = validacao_pergunta()

        if pergunta == "n":
            return

#Listar produtos
def listar_produtos(estoque):
    print("Você optou listar os produtos do estoque\n")

    for i in estoque:
        print(f'Descrição: {i['descricao']}, Código: {i['codigo']}, Estoque: {i['quantidade']}, Custo: {i['custoItem']}, Preço de venda: {i['precoVenda']} ')

#ordenar de forma decrescente pela quantidade em estoque
def ordenar_produtos(estoque):
    print("Você optou ordenar os produtos do estoque\n")

    produtos_ordenados = sorted(estoque, key=lambda p: p["quantidade"], reverse=True)
    for produto in produtos_ordenados:
        print(f'Descrição: {produto['descricao']}, Código: {produto['codigo']}, Estoque: {produto['quantidade']}, Custo: {produto['custoItem']}, Preço de venda: {produto['precoVenda']} ')

#buscar produtos
def buscar_produtos():
    print("Você optou buscar um produto\n")

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

#remover produtos
def remover_produtos():
    print("Você optou remover um produto\n")

    global estoque

    while True:
        try:
            index = int(input("Digite o código do produto a ser removido:\n"))
            produto_encontrado = False

            for idx, produto in enumerate(estoque):
                if produto["codigo"] == index:
                    print(f"Produto excluído: {produto}")
                    del estoque[idx]
                    produto_encontrado = True
                    print(f"Estoque atualizado:\n{estoque}")

                    pergunta = validacao_pergunta()
                    if pergunta == "n":
                        return  
                    break

            if not produto_encontrado:
                print("Produto não encontrado.")

        except ValueError:
            print("Erro: Digite apenas números para o código do produto.")

#consultar produtos esgotados
def consultar_produtos_esgotados(estoque):
    print("Você optou consultar produtos esgotados\n")

    for i in estoque:
        if i["quantidade"] == 0:
            print(i)

#Filtro de produtos com baixa quantidade
def filtro_baixa_quantidade(estoque):
    print("Você optou consultar produtos com baixa quantidade em estoque\n")

    for i in estoque:
        if i["quantidade"] < flag_baixa_quantidade:
            print(i)

#Atualizar estoque
def atualizar_quantidade():

    print("Você optou por atualizar a quantidade em estoque de um produto\n")

    global estoque

    while True:
        produto = achar_produtos()
        print("Produto encontrado: ", produto)
        
        operacao = somar_ou_subtrair()
        while True: 
            quantidade = validar_nova_quantidade()
            
            if operacao == 1:
                produto["quantidade"] += quantidade
                print(f"Quantidade atualizada: {produto}")
                break  
            
            else:  
                if produto["quantidade"] < quantidade:
                    print("Erro: A quantidade retirada não pode ser maior que o estoque. Tente novamente.")
                else:
                    produto["quantidade"] -= quantidade
                    print(f"Quantidade atualizada: {produto}")
                    break  

        pergunta = validacao_pergunta() 
        if pergunta == 'n':
            break

#Atualização de preços
def atualizar_preco():
    print("Você optou por atualizar o preço de um produto\n")

    global estoque

    while True:
        produto = achar_produtos()
        print("Produto encontrado: ", produto)
        
        while True:  
            novoPreco = validar_preco_novo()
            
            if novoPreco > produto['custoItem']:
                produto["precoVenda"] = novoPreco
                print(produto)
                break  
            else:
                print("O novo preço de venda deve ser maior que o preço de custo")
        
        break  
                
# Calcular Total estoque
def total_estoque(estoque):
    print("Você optou por ver o preço bruto do estoque\n")

    arrayTotais = []

    for i in estoque:
        resultado = i["quantidade"] * i["precoVenda"]
        arrayTotais.append(resultado)

    return sum(arrayTotais)

#Calcula o lucro presumido subtraindo o total da soma de custo do total sa soma de preços de venda
def lucro_presumido(estoque):
    print("Você optou por ver o lucro do estoque\n")

    arraysCustos = []

    for i in estoque:
        arraysCustos.append(i["custoItem"])
    return total_estoque(estoque) - sum(arraysCustos)

def exibir_relatorio(estoque):

    print("Descrição".ljust(20) + "Código".ljust(10) + "Quantidade".rjust(12) +
          "Custo".rjust(10) + "Preço".rjust(10) + "Valor Total".rjust(15))
    print("=" * 77)
    
    custo_total = 0
    faturamento_total = 0
    
    for item in estoque:
        descricao = item['descricao'].ljust(20)
        codigo = str(item['codigo']).ljust(30)
        quantidade = str(item['quantidade']).rjust(12)
        custo = f"{item['custoItem']:.2f}".rjust(10)
        preco = f"{item['precoVenda']:.2f}".rjust(10)
        valor_total = item['quantidade'] * item['precoVenda']
        
        custo_total += item['quantidade'] * item['custoItem']
        faturamento_total += valor_total
        
        valor_total_str = f"{valor_total:.2f}".rjust(15)
        print(descricao + codigo + quantidade + custo + preco + valor_total_str)
    
    print("=" * 77)
    print(f"{'Custo Total:':<45}{custo_total:>32.2f}")
    print(f"{'Faturamento Total:':<45}{faturamento_total:>32.2f}")


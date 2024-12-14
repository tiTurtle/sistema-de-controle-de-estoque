estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;0;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

def tratar_dados_estoque(estoque):
    estoque_inicial_lista = estoque.split("#")

    estoque_inicial_lista2 = []
    for i in estoque_inicial_lista:
        produtoEpropriedades = i.split(";")
        estoque_inicial_lista2.append(produtoEpropriedades)

    for i in estoque_inicial_lista2:
        i[1] = float(i[1])
        i[2] = float(i[2])
        i[3] = float(i[3])
        i[4] = float(i[4])

    estoque_inicial_campos = ['descricao', 'codigo', 'quantidade', 'custoItem', 'precoVenda']

    estoque_inicial_lista_de_dicionarios = []

    for i in estoque_inicial_lista2:
        estoque_inicial_lista_de_dicionarios.append(dict(zip(estoque_inicial_campos, i)))

    return estoque_inicial_lista_de_dicionarios

estoque = tratar_dados_estoque(estoque_inicial)

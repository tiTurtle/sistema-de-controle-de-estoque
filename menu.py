from funcoes_principais import *
from funcoes_auxiliares import *

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("[1] - Adicionar um produto")
        print("[2] - Listar produtos")
        print("[3] - Ordenar produtos por quantidade em estoque")
        print("[4] - Buscar um produto específico")
        print("[5] - Remover produto")
        print("[6] - Consultar produtos esgotados")
        print("[7] - Filtrar produtos com baixa quantidade")
        print("[8] - Atualizar quantidade de um produto específico")
        print("[9] - Atualizar preço de um produto específico")
        print("[10] - Ver o valor total do estoque")
        print("[11] - Ver o lucro presumido")
        print("[12] - Exibir relatório")
        print("[0] - Sair do menu")

        opcao = validar_opcao_menu()

        match opcao:
            case 1: cadastro_produtos()
            case 2: listar_produtos(estoque)
            case 3: ordenar_produtos(estoque)
            case 4: printar(buscar_produtos())
            case 5: remover_produtos()
            case 6: consultar_produtos_esgotados(estoque)
            case 7: filtro_baixa_quantidade(estoque)
            case 8: atualizar_quantidade()
            case 9: atualizar_preco()
            case 10: print(f"Valor total do estoque: R$ {total_estoque(estoque):.2f}")
            case 11: print(f"Lucro presumido: R$ {lucro_presumido(estoque):.2f}")
            case 12: print(f"Relatório {exibir_relatorio(estoque)}")
            case 0:
                print("Saindo do menu...")
                return

menu()
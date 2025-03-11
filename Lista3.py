# Lista laço for para iterar sobre cada item da lista e imprimir na tela
def main():
    # Inicializa a lista de compras com 5 itens 
    lista_de_compras = ["requeijão", "goiaba", "óleo", "banana", "amaciante"]

    # Exibe todos os itens da lista usando um laço de repetição
    print("Lista de Compras:")
    for item in lista_de_compras:
        print(f"- {item}")

# Executa a função principal
if __name__ == "__main__":
    main()

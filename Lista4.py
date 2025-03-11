# Lista Cidades 
def main():
    # Inicializa uma lista vazia para as cidades
    cidades = []

    # Solicita 3 nomes de cidades ao usuário
    print("Digite o nome de 3 cidades brasileiras:")
    for i in range(3):
        cidade = input(f"Cidade {i+1}: ")
        cidades.append(cidade)

    # Exibe a lista de cidades
    print("Lista de Cidades:")
    for cidade in cidades:
        print(f"- {cidade}")


if __name__ == "__main__":
    main()

# Lista nomes 
def main():
    # Inicializa uma lista vazia para os nomes
    nomes = []

    # Solicita 5 nomes ao usuário
    print("Digite 5 nomes de atletas olímpicos:")
    for i in range(5):
        nome = input(f"Nome {i+1}: ")
        nomes.append(nome)

    # Exibe a lista de nomes
    print("Lista de Nomes dos atletas olímpicos:", nomes)

    # Solicita um número de 0 a 4 para remover um elemento
    try:
        posicao = int(input("Digite um número de 0 a 4 para remover o nome do atleta que você menos gosta: "))
        if 0 <= posicao < len(nomes):
            nome_removido = nomes.pop(posicao)
            print(f"O nome '{nome_removido}' foi removido da lista.")
        else:
            print("Número fora do intervalo permitido.")
    except ValueError:
        print("Por favor, digite um número válido.")

    # Exibe a lista atualizada de nomes
    print("Lista Atualizada de Nomes:", nomes)


if __name__ == "__main__":
    main()

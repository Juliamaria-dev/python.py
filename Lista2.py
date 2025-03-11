# Lista de Solicitação de 1o números pares 
def main():
    # Inicializa uma lista vazia
    numeros = []

    # Solicita 10 inteiros ao usuário
    print("Digite 10 números inteiros:")
    for i in range(10):
        numero = int(input(f"Número {i+1}: "))
        numeros.append(numero)

    # Exibe a lista de números
    print("A lista de números é:", numeros)

    # Conta quantos valores pares existem na lista
    contagem_pares = sum(1 for num in numeros if num % 2 == 0)

    # Exibe a quantidade de números pares
    print(f"A quantidade de valores pares na lista é: {contagem_pares}")


if __name__ == "__main__":
    main()

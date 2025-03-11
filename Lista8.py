# Lista de números em posições na lista 
def main():
    # Inicializa uma lista vazia para os números
    numeros = []

    # Solicita 5 números inteiros ao usuário
    print("Digite 5 números inteiros:")
    for i in range(5):
        numero = int(input(f"Número {i+1}: "))
        numeros.append(numero)

    # Exibe cada número com sua posição na lista
    print("Números e suas posições:")
    for indice, numero in enumerate(numeros):
        print(f"Posição {indice}: {numero}")

if __name__ == "__main__":
    main()


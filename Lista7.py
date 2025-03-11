# Lista números na ordem inversa 
def main():
    # Inicializa uma lista vazia para os números
    numeros = []

    # Solicita 10 números reais ao usuário
    print("Digite 10 números reais:")
    for i in range(10):
        numero = float(input(f"Número {i+1}: "))
        numeros.append(numero)

    # Exibe os números na ordem inversa
    print("Números na ordem inversa:")
    for numero in reversed(numeros):
        print(numero)

if __name__ == "__main__":
    main()

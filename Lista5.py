# Lista que permite ao usuário verificar se o seu número está presente nessa lista 
def main():
    # Inicializa a lista com alguns números diferentes
    numeros = [10, 25, 37, 42, 58, 74, 89, 100]

    # Solicita um número ao usuário
    numero_verificar = int(input("Digite o número do seu ingresso para verificar se está na lista da festa: "))

    # Verifica se o número está na lista
    if numero_verificar in numeros:
        print(f"O número {numero_verificar} está na lista.")
    else:
        print(f"O número {numero_verificar} não está na lista.")


if __name__ == "__main__":
    main()

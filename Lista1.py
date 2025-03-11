# Lista 10 números 
def main():
    
    numeros = []

    # Solicita o número da senha do usuário
    print("Digite 10 números da sua senha:")
    for i in range(10):
        numero = int(input(f"Número {i+1}: "))
        numeros.append(numero)

    # Solicita o número a ser verificado
    numero_para_verificar = int(input("Digite o dia da sua data de nascimento para verificar se está na lista de pendências no pagamento mensal: "))

    # Verifica se o número está na lista
    if numero_para_verificar in numeros:
        print(f"O número {numero_para_verificar} está pendente, favor tratar na agência bancária mais próxima.")
    else:
        print(f"O número {numero_para_verificar} não está na lista de pendências.")

# Executa a função principal
if __name__ == "__main__":
    main()

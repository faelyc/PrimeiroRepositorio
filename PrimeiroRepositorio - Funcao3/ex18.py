# 18. Crie uma função ler_inteiro() que solicita ao usuário um número inteiro.
# Se o usuário inserir um valor inválido (não inteiro), exiba uma mensagem
# e peça a entrada novamente até que um número válido seja fornecido.

def ler_inteiro():
    while True:
        try:
            numero = int(input("Por favor, insira um número inteiro: "))
            return numero
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")


numero = ler_inteiro()
print(f"Você inseriu o número inteiro: {numero}")
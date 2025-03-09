# 28 Peça para o usuário digitar um número e exiba o fatorial desse número.
numero = (int(input("Digite um número:")))

def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é", resultado)
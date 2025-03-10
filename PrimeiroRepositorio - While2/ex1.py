# 1. Solicite ao usuário um número inteiro positivo e exiba apenas os números pares de 2 até esse número.
num = int(input("Digite um número inteiro positivo: "))




while num < 0:
    num = int(input("Digite um número inteiro positivo: "))

    if num < 0:
        print("Número inválido. Digite um número inteiro positivo.")

for i in range(2, num + 1, 2):
    print(i, end=" ")
# 37 Faça um programa que peça um número inteiro e determine se ele é ou
# não um número primo. Um número primo é aquele que é divisível somente
# por ele mesmo e por 1.

num = int(input("Digite um numero inteiro:"))

# Não primo

# - pares

# - menor de 2

# - divididos por um contador que de 0

if num < 2:
    print("Nao e primo")
else:
    for i in range(2, num+1):
        if num % i == 0:
            print("Nao e primo")
            break
        else:
            print("E primo")
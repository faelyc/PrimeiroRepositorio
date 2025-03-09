# 1. Leia dois números, faça a soma e apresente caso seja maior que 15.

num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número:"))
soma = num1 + num2
if soma > 15:
  print("A soma é:", soma)
# 34 Faça um programa que receba um número e usando laços de repetição
# calcule e mostre a tabuada desse número.


numero = int(input("Digite um numero:"))


for i in range(1,11,1):

  print(f" {numero} x {i} = {numero*i}")
  resultado = (numero*i)
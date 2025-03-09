# 13 Peça para o usuário digitar um número e exiba a sua tabuada de 1 a 10.


numero = int(input("Digite um numero:"))


for i in range(1,11,1):

  print(f" {numero} x {i} = {numero*i}")
  resultado = (numero*i)
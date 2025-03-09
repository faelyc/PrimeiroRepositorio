# 12. Faça um Programa que leia um número e exiba o dia correspondente da
# semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido


numero = int(input("Digite o numero de 1 a 7:"))

match numero:
  case 1:
    print("Domingo")
  case 2:
    print("Segunda")
  case 3:
    print("Terca")
  case 4:
    print("Quarta")
  case 5:
    print("Quinta")
  case 6:
    print("Sexta")
  case 7:
    print("Sabado")
  case _:
    print("Numero invalido, digite um numero entre 1 e 7")
# 2. Crie um programa que leia a idade de uma pessoa e imprima:
# "Criança" se a idade for menor que 12;
# • "Adolescente" se estiver entre 12 e 17;
# • "Adulto" se estiver entre 18 e 64;
# • "Idoso" se for 65 ou mais.


idade = int(input("Insira sua idade"))

if idade <12:
  print("Criança")
elif idade >=12 and idade <=17:
  print("Adolescente")
elif idade >=18 and idade <=64:
  print("Adulto")
else:
  print("Idoso")
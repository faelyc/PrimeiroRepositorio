#8) Faça um programa que solicite o nome e a idade do usuário e informe se ele é maior de
#idade ou não.
nome = (input("Informe o nome: "))
idade = (int(input("Informe a idade: ")))

if idade >= 18:
  print("Maior de idade")
else:
  print("Menor de idade")
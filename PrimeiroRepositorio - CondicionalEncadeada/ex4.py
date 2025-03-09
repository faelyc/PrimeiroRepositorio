# 4 Crie um programa que calcule o bônus de um funcionário com base
# no tempo de serviço:
# • Sem bônus para menos de 1 ano;
# • Bônus de 5% para 1 a 3 anos;
# • Bônus de 10% para 3 a 5 anos;
# • Bônus de 15% para mais de 5 anos.
# • Solicite o salário e o tempo de serviço, e exiba o salário final com
# bônus (se aplicável).
salario = float(input("Insira seu salario:"))
tempo = float(input("Insira seu tempo de servico: "))


if tempo <1:
  print("Sem bonus")
elif tempo >=1 and tempo <3:
  print("Bonus de 5%")
elif tempo >3 and tempo <5:
  print("Bonus de 10%")
else:
  print("Bonus de 15%")

calculo = salario * tempo
print("Salario", calculo)
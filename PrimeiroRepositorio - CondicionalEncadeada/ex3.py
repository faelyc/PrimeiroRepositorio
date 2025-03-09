# 3 Desenvolva um programa que calcule o IMC (Índice de Massa
# Corporal) de uma pessoa e classifique-a como:
# • "Abaixo do peso" se IMC < 18.5;
# • "Peso normal" se 18.5 ≤ IMC < 25;
# • "Sobrepeso" se 25 ≤ IMC < 30;
# • "Obesidade" se IMC ≥ 30.
# Receba o peso (kg) e a altura (m) do usuário.

peso = float(input("Insira seu peso:"))
altura = float(input("Insira sua altura:"))

calculo = peso / altura * altura
print("Seu IMC e:", calculo)


if calculo <18.5:
  print("Abaixo do peso")
elif calculo >= 18.5 and calculo <25:
  print("Peso Normal")
elif calculo >=25 and calculo <30:
  print("Sobrepeso")
else:
  print("Obesidade")
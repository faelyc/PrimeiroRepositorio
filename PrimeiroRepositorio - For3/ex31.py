# 31 Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

lista = []
numero1 = int(input("Digite um numero :"))
numero2 = int(input("Digite um numero :"))

for i in range(numero1, +1 ,numero2):
  numero1.append(i)
  numero2.append(i)
  print(i)
print("Soma do intervalo:", sum(lista))

numero1=int(input("digite um numero:"))
numero2=int(input("digite outro numero: "))

while numero2 < numero1:
	numero1=int(input("digite um numero: "))
	numero2=int(input("digite outro numero: "))
	break
else:
	for i in range(numero1, numero2, 1):
		print(i)





for c in range(1,51):
 if c % 2 != 0:
  print(c)
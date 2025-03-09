# 30 Faça um programa que leia 5 números e informe o maior número.



maior = -999999
for n in range(5):
  numero = int(input(f'Número #{n+1}:'))
  if numero > maior:
    maior = numero

print('Maior =',maior)
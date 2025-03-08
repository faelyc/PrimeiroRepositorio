#7) Faça um programa que converta um valor em reais para dólares. O usuário informará o
#valor em reais e a taxa de câmbio.

valorreal = float(input("Digite um valor em real:"))
taxacambio = float(input("Digite o valor da taxa de câmbio:"))

resultado = valorreal / taxacambio
print(resultado)
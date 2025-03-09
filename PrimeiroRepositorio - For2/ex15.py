# 15 Solicite que o usuário digite 5 números e exiba a média aritmética deles.

for i in range(5):
  numero = int(input("digite um numero:"))
  print(i)

media = (numero + numero + numero + numero + numero) / 2
print(f"A média dos numeros é: {media}")
#10. Apenas aceitar números positivos. O programa deve continuar pedindo
#um número até o usuário digitar um número positivo.

num = -1


while num <= 0:
  num = int(input("Digite um número positivo: "))

  if num >= 0:
    print("Número válido. ")

  else:
    print("Número inváldo. Digite um número positivo!")
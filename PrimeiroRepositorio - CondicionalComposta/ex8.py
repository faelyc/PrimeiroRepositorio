# 8. Verificação de múltiplo de 5
#Peça um número ao usuário e verifique se ele é múltiplo de 5. Se for,
#exiba Múltiplo de 5, senão exiba Não é múltiplo de 5.
n = int(input("Insira um numero:"))

if n % 5 == 0:
  print("Esse numero e multiplo de 5")
else:
  print("O numero nao e multiplo de 5")
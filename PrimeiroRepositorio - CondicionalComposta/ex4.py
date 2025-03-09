# 4. Verificação de nome em lista
#Peça um nome ao usuário. Se for Carlos, exiba Você está na lista,
#senão, exiba Nome não encontrado.


senha = input("Digite seu nome:").lower().strip()

if senha == "1234":
  print("Senha valida")
else:
  print("Senha invalida")
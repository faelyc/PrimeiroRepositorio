# 6. Escreva um programa que verifique a validade de uma senha fornecida pelo
# usuário. A senha válida é o número 1234. Devem ser impressas as seguintes
# mensagens:
# ACESSO PERMITIDO caso a senha seja válida.
# ACESSO NEGADO caso a senha seja inválida.


senha = input("Insira a senha:")

if senha == "1234":
  print("Acesso permitido")
else:
  print("Acesso Negado")
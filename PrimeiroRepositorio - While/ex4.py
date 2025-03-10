# 4 O usuário deve digitar a senha correta (1234). Enquanto errar, o
# programa deve pedir novamente.

senha = "1234"
tentativa = input("Digite a senha:")

while senha != tentativa:
  print("Senha errada, tente novamente:")
  tentativa = input("Digite a senha:")
print("Acesso autorizado")
# 7. Verificação de turno
#Peça ao usuário para digitar M; para manhã ou qualquer outra tecla
#para tarde. Se for M, exiba Bom dia!, senão exiba Boa tarde!.
turno = input("Insira M para manha ou qualquer outra tecla para tarde").upper()

if turno == "M":
  print("Bom dia")
else:
  print("Boa tarde")
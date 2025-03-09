# 3. Autorização de entrada em um evento
#Se a pessoa tiver um convite válido, exiba Entrada permitida, caso
#contrário, exiba Entrada negada.
convite = input("voce tem um convite valido? (S/N):").upper()

if convite == "S":
  print("Entrada permitida")
else:
  print("Entrada negada")
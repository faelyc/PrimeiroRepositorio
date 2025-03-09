#Escreva um programa em Python que:
#• Solicite ao usuário que insira seu tipo (militar, cientista, civil, hacker ético).
#• Solicite as informações adicionais necessárias para cada caso (nível de
#segurança, autorização, dia da semana, etc.).
#• Decida se a pessoa pode ou não entrar, exibindo uma mensagem apropriada

tipoUsuario = input("Digite o tipo de usuário (militar, cientista, civil, hacker ético): ").strip().lower()

if tipoUsuario == "militar":
  patente = input("Informe a patente (general ou soldado): ").strip().lower()
  if patente == "general":
    print("Acesso concedido.")
  elif patente == "soldado":
    emmissao = input("O soldado está em missão? (sim/não) :").strip().lower()
    acompanhado = input("O soldado está acompanhado de um oficial superior? (sim/não): ").strip().lower()
    if emmissao == "sim" and acompanhado == "sim":
      print("Acesso concedido.")
    else:
      print("Acesso negado.")
  else:
    print("A patente é inválida para o acesso.")

elif tipoUsuario == "cientista":
  autorizacao = input("O cientista possui a autorização secreta ? (sim/não): ").strip().lower()
  if autorizacao == "sim":
    print("Acesso concedido")
  else:
    nivelSeguranca = int(input("Informe o nível de segurança: ")).strip().lower()
    if nivelSeguranca >= 5:
      print("Acesso concedido.")
    else:
      escolta = input("O cientista está acompanhado por escolta militar ? (sim/não)")
      if escolta == "sim":
        print("Acesso concedido.")
      else:
        print("Acesso negado.")


elif tipoUsuario == "civil":
  familiarMilitar = input("O civil é familiar direto de um militar de alta patente? (sim/não): ").strip().lower()
  if familiarMilitar == "sim":
    print("Acesso concedido")
  else:
    diaSemana = input("Qual o dia da semana ? :").strip().lower()
    if diaSemana in ["segunda-feira", "quinta-feira"]:
      print("Acesso concedido")
    else:
      print("Acesso negado")

elif tipoUsuario == "hacker ético":
  codigoAcesso = input("Possui um código de acesso válido? (sim/não) :")
  if codigoAcesso == "sim":
    print("Acesso concedido.")
  else:
    acompanhado = input("O hacker do bem está acompanhado por um militar de nível superior ? (sim/não): ").strip().lower()
    if acompanhado == "sim":
      print("Acesso concedido.")
    else:
      print("Acesso negado.")

else:
  print("O usuário não é digno de entrar na zona de segurança.")
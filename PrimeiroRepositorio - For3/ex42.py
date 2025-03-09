# 42 Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

nota = int(input("Digite uma nota entre zero e dez:"))
if nota > 1:
    print("Valor inválido")
if nota == 0:
    print("Valor valido:")
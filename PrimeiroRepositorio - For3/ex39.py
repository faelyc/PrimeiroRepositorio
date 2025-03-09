# 39 Faça um programa que peça para n pessoas a sua idade, ao final o
# programa deverá verificar se a média de idade da turma varia entre 0 e
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou
# idosa, conforme a média calculada.
idade = (int(input("DIgite sua idade:")))

if idade <= 26:
    print("Jovem")
elif idade > 26:
    print("Adulta")
else:
    print("Idoso")
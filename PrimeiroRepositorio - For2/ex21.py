# 21 Solicite ao usuário um número e exiba os 10 primeiros múltiplos desse número.


numero = (int(input("Digite um número:")))
n = 10
multiplos = []

multiplos = [ 3 * i for i in range(1, n + 1) ]
print(multiplos)
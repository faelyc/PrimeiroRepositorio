# 27 Solicite um número ao usuário e exiba um triângulo numérico crescente.


numero = int(input("Digite um numero:"))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end="")
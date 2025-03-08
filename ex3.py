#3) Elaborar um algoritmo que solicite os dados de estatura (em metros) e peso (em Kg) de
#uma pessoa e calcule/visualize seu IMC (Índice de Massa Corporal):
estatura = float(input("Digite sua estatura:"))
peso = float(input("Digite seu peso:"))

resultado = peso / estatura ** 2
print(resultado)
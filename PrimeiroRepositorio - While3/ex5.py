#5. Escreva um programa que leia um número inteiro positivo e determine se ele é um
#quadrado perfeito (ou seja, se existe um número inteiro x tal que x² = n).
#Exemplo:
#Entrada: 49
#Cálculo: 7 × 7 = 49
#Saída: 49 é um quadrado perfeito

num = int(input("Digite um número inteiro positivo: "))
contador = 0

while contador**2 < num: 
    contador += 1

if contador**2 == num: 
    print(f"O número {num} é um quadrado perfeito! Sua raiz quadrada é {contador}.")

else:
    print(f"O número {num} não é um quadrado perfeito!")
#  7. Adivinhe o número secreto (de 1 a 10). O usuário deve tentar adivinhar
# um número até acertar. (Declare um valor e receba outro)
palpite = int(input("Tente adivinhar o número: "))
numero_secreto = 10

if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
    
elif palpite > numero_secreto:
    print("Tente um número menor.")
else:
    print("Tente um número maior.")

tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    
    tentativas += 1

if tentativas == max_tentativas:
    print(f"Fim do jogo. O número era {numero_secreto}.")
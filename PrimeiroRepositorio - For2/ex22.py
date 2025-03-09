# 22 Peça ao usuário para digitar uma palavra e exiba quantas vogais ela contém.

palavra = (input("Digite uma palavra:")) .lower()
vogais = "aeiou"
quantidadedevogais = 0

for letra in palavra:
  if letra in vogais:
    quantidadedevogais += 1

print(f"A palavra {palavra} tem {quantidadedevogais} vogais")
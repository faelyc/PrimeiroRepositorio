# 29 Solicite uma frase e uma letra ao usuário e exiba quantas vezes essa letra aparece na frase.



frase = input("Digite uma frase:").lower()
letra = input("Digite uma letra:").lower()
vogais = "aeiou"
quantidadedeletras = 0

for letra in frase:
  if letra in frase:
    quantidadedeletras += 1

print(f"A frase {frase} tem {quantidadedeletras} letras")
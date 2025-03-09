# Exercício 9: Crie uma função que conte quantas vogais existem em uma string
# fornecida.

def contar_vogais(s):
    vogais = "aeiou"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador


string = "Teste"
print(f"Quantidade de vogais: {contar_vogais(string)}")
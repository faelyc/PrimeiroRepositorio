# 14. Crie uma função que recebe uma lista de palavras e junta tudo em uma
# única frase.

def juntar_palavras(lista_palavras):
    return ' '.join(lista_palavras)

palavras = ["Olá", "mundo"]
frase = juntar_palavras(palavras)
print(frase)
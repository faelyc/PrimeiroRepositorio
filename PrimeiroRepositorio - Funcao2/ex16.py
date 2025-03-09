# 16. Crie uma função que recebe uma lista de palavras e retorna a palavra
# com mais letras.

def palavra_maior(lista_palavras):
    if not lista_palavras:
        return None
    return max(lista_palavras, key=len)

palavras = ["casa", "paralelepipedo", "pindamonhangaba", "bicicleta"]
print(palavra_maior(palavras))
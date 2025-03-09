# Exercício 7: Crie uma função que receba uma lista de números e retorne o
# maior número dessa lista.


def maior_numero(lista):
    if not lista:
        return None
    maior_numero = lista[0]
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero


numeros = [3, 5, 7, 2, 8, 1]
print(maior_numero(numeros))
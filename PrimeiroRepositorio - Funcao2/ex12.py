# 12. Crie uma função que recebe uma lista de números e retorna a
# quantidade de números positivos.


def contar_numeros_positivos(lista):
    return len([num for num in lista if num > 0])
numeros = [-1, 0, 5, 2, 8]
quantidade_positivos = contar_numeros_positivos(numeros)
print(quantidade_positivos)
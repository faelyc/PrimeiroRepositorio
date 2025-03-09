# 15. Crie uma função que recebe uma lista de números e substitui os
# números negativos por zero.

def numeros_negativos(lista):
    return [max(0, num) for num in lista]

numeros = [-5, 3, -1, 7, -2]
resultado = numeros_negativos(numeros)
print(resultado)
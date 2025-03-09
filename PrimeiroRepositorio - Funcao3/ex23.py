# 23. Crie uma função pegar_elemento(lista, indice) que retorna o elemento
# de uma lista na posição indice.
# Se o índice não existir, trate o erro.


def pegar_elemento_lista(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Índice fora do alcance da lista."

minha_lista = [10, 20, 30, 40, 50]
print(pegar_elemento_lista(minha_lista, 2))
print(pegar_elemento_lista(minha_lista, 10))
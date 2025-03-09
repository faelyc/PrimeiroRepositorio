# 21. Crie uma função soma_lista(numeros) que recebe uma lista de números
# e retorna a soma.
# Se a lista contiver valores inválidos, capture a exceção e exiba uma
# mensagem de erro.

def soma_lista_numeros(lista):
    try:
        return sum(lista)
    except IndexError:
        return "Erro."

numeros = [1, 2, 3, 4, 5]
resultado = soma_lista_numeros(numeros)
print(f"A soma dos números na lista é: {resultado}")
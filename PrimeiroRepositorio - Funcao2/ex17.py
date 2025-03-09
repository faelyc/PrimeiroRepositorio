# 17. Crie uma função que recebe uma lista de números e retorna a soma
# apenas dos números pares.
def soma_pares(numeros):
    return sum(num for num in numeros if num % 2 == 0)

lista = [1, 2, 3, 4]
resultado = soma_pares(lista)
print(resultado)
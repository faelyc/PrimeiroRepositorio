# 22. Crie uma função multiplicar(a, b) que retorna o produto de a e b.
# Se os valores não forem números, capture a exceção e exiba uma
# mensagem de erro.



def multiplicar(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Erro: Ambos os valores devem ser números."


print(multiplicar(5, 3))
print(multiplicar(5, '3'))
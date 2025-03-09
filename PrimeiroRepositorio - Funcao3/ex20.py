# 20. Crie uma função divisao_segura(a, b) que retorne o resultado da divisão
# a / b.
# Se b for zero, a função deve retornar Erro: Divisão por zero não
# permitida!.


def divisao_segura(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Erro "
    except TypeError:
        return "Divisão por zero não é permitida"
    return resultado

print(divisao_segura(10, 2))
print(divisao_segura(10, 0))
print(divisao_segura(10, 'a'))
# Exercício 2: Crie uma função que receba um número e retorne Par se o
# número for par ou Ímpar; se o número for ímpar.
def numero(valor):
    if valor % 2 == 0:
      return "Par"
    else:
      return "Impar"
print(numero(10))
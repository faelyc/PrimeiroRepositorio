# Exercício 6: Crie uma função que receba uma string e retorne True se ela for
# um palíndromo (uma palavra ou frase que se lê da mesma forma de trás para
# frente) e False caso contrário.

def palindromo(s):

    s = ''.join(s.split()).lower()

    return s == s[::-1]


print(palindromo("Asa"))
print(palindromo("Esse"))
# 24. Crie uma função contar_caracteres(texto, caractere) que conta quantas
# vezes um caractere aparece em um texto.
# Se texto não for uma string, exiba um erro.



def contar_caracteres(texto, caractere):

    try:
        return texto.count(caractere)
    except IndexError:
        return "Erro."

texto = "guaratingueta"
caractere = "a"
quantidade = contar_caracteres(texto, caractere)
print(f"O caractere '{caractere}' aparece {quantidade} vezes no texto.")
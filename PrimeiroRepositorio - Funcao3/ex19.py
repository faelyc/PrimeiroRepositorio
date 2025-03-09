# 19. Crie uma função calcular_media(numeros) que recebe uma lista de
# números e retorna a média.
# Se a lista estiver vazia, a função deve tratar a exceção e exibir uma
# mensagem adequada.

def calcular_media_numeros(lista_numeros):
    if not lista_numeros:
        return 0
    soma = sum(lista_numeros)
    quantidade = len(lista_numeros)
    media = soma / quantidade
    return media


numeros = [10, 20, 30, 40, 50]
media = calcular_media_numeros(numeros)
print(f"A média dos números é: {media}")
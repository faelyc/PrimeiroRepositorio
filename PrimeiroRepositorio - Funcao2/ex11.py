# 11. Crie uma função que recebe duas palavras e retorna True se forem
# anagramas uma da outra.


def sao_anagramas(palavra1, palavra2):

    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()


    if len(palavra1) != len(palavra2):
        return False

    return sorted(palavra1) == sorted(palavra2)


print(sao_anagramas("amor", "roma"))
print(sao_anagramas("python", "typhon"))
print(sao_anagramas("teste", "texto"))
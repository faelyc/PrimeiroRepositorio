# 8. Desenvolva um programa que recebe do usuário o placar de um jogo de
# futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória
# foi do primeiro time ou do segundo time.


gols_time1 = int(input("Gols do primeiro time: "))
gols_time2 = int(input("Gols do segundo time: "))
if gols_time1 > gols_time2:

    print("Vitória do primeiro time")
elif gols_time1 < gols_time2:
    print("Vitória do segundo time")
else:
    print("Empate")
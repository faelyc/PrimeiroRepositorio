#  44 Faça um programa que receba a idade de 15 pessoas e que calcule e
# mostre:
# a) A quantidade de pessoas em cada faixa etária;
# b) A percentagem de pessoas na primeira e na última faixa etária, com
# relação ao total de pessoas:
# Até 15 anos
# De 16 a 30 anos
# De 31 a 45 anos
# De 46 a 60 anos
# Acima de 61 anos

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range (0,5):
    idadestr = input("digite a idade da pessoa")
    idade = int(idadestr)
    if idade <= 15:
        faixa1 += 1
    elif idade > 15 and idade < 30:
        faixa2 += 1
    elif idade >30 and idade <45:
        faixa3 += 1
    elif idade > 45 and idade <60:
        faixa4 += 1
    else:
        faixa5 += 1


print ("até 15 anos", faixa1)
print("De 16 a 30 anos", faixa2)
print("De 31 a 45 anos", faixa3)
print ("De 46 a 60 anos", faixa4)
print ("acima de 61 anos", faixa5)
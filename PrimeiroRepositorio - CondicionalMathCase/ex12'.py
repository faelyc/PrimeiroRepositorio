# 12. Faça um Programa que leia um número e exiba o dia correspondente da
# semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido


dia = int(input("Digite um número (1-7): "))
dias = {

    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
        
        }
print(dias.get(dia, "Valor inválido"))
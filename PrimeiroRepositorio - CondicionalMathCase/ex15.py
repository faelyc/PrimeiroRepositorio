# 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# “Telefonou para a vítima? “
# “Esteve no local do crime?”
# “Mora perto da vítima? “
# “Devia para a vítima? “
# “Já trabalhou com a vítima? “
# 16. O programa deve no final emitir uma classificação sobre a participação da
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
# ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como
# “Assassino “. Caso contrário, ele será classificado como “Inocente “.

perguntas = [
"Telefonou para a vítima? (s/n) ",
"Esteve no local do crime? (s/n) ",
"Mora perto da vítima? (s/n) ",
"Devia para a vítima? (s/n) ",
"Já trabalhou com a vítima? (s/n) ";
]
respostas = [input(p).strip().lower() == "s" for p in perguntas]
total_positivas = sum(respostas)
if total_positivas == 2:
    print("Suspeita")
elif 3 <= total_positivas <= 4:
    print("Cúmplice")
elif total_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
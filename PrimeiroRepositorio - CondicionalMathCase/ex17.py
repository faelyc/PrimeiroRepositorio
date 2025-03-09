# 17. Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))
menor_preco = min(preco1, preco2, preco3)
if menor_preco == preco1:
    print("Compre o primeiro produto")
elif menor_preco == preco2:
    print("Compre o segundo produto")
else:
    print("Compre o terceiro produto")
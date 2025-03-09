# 43 Uma loja tem tem uma política de descontos de acordo com o valor da
# compra do cliente. Os descontos começam acima dos R$500. A cada 100
# reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até
# 25%.
# Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
# Faça um programa que exiba essa tabela de descontos no seguinte formato:
# Valordacompra – porcentagem de desconto – valor final



valordacompra= float(input('Valor da compra:'))
des1 = float(valordacompra*0.01)
des2 = float(valordacompra*0.02)
print (f'O desconto é de R${des1:.2f} e o valor final é R${des2:.2f}')
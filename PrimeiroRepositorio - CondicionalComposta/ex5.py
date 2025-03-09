# 5. Cálculo de gorjeta
#Peça o valor da conta. Se for maior que R$100,00, adicione uma gorjeta
#de 10% e exiba o total a pagar. Caso contrário, adicione uma gorjeta de
#5%.
conta = float(input("Insira o valor da conta:"))

if conta > 100:
  gorjeta = conta*0.10
else:
  gorjeta = conta*0.05
total = conta + gorjeta
print(f"Total a pagar: R${total:.5f}")
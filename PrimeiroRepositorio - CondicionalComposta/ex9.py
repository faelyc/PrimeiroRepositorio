# 9. Desconto em compras por valor mínimo
#Se o valor da compra for maior que R$150,00, aplique um desconto de
#R$20,00. Caso contrário, não aplique desconto.
valorconsumido = float(input("Digite o valor da compra:"))

if valorconsumido > 150:
  valorcomdesconto = valorconsumido - 20
  print("O valor com desconto e de:", valorcomdesconto,"R$")
else:
  print("O valor fica em:", valorconsumido, "R$")
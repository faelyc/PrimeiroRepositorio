# 38. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja A
# foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse
# valor mostre na tela uma mensagem contendo em quanto foi superado o
# faturamento.


i = 0
acumulado = 0
if i < 5:
    valor = float(input("Digite o valor de compra do cliente " + str(i)))
    acumulado = acumulado + valor
    i += 1

if acumulado > 54000:
    print("Superou! em: ", 54000 - acumulado )
else:
    print("não superou")
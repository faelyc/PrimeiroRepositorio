#4) Solicitar ao usuário que informe o comprimento, a largura e a altura de uma caixa
#retangular. Apresentar o volume de uma caixa retangular. Apresentar o volume de uma caixa
#retangular por meio da fórmula: Volume <- Comprimento * Largura * Altura

comprimento = float(input("Digite o comprimento:"))
largura = float(input("Digite a largura:"))
altura = float(input("Digite a altura:"))

resultado = comprimento * largura * altura
print(resultado)
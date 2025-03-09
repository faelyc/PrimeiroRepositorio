# 13. Faça um programa que pergunte ao usuário se ele quer passar uma
# temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a
# partir da resposta do usuário, faça a devida conversão.


opcao = input("Converter (F)ahrenheit para Celsius ou (C)elsius para Fahrenheit? ").upper()
if opcao == "F":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Temperatura em Celsius: {c:.2f}°C")
elif opcao == "C":
    c = float(input("Digite a temperatura em Celsius: "))
    f = (c * 9/5) + 32
    print(f"Temperatura em Fahrenheit: {f:.2f}°F")
else:
    print("Opção inválida!")
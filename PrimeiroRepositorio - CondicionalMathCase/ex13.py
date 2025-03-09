# 13. Faça um programa que pergunte ao usuário se ele quer passar uma
# temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a
# partir da resposta do usuário, faça a devida conversão.


c = float(input("Informe a temperatura em °C:"))
f = 9 * c / 5 + 32
print("A temperatura de {}°C corresponde a {} °F:" .format (c, f))



f = float(input("Informe a temperatura em °F:"))
c = f - 32 * 5 / 9
print("A temperatura de {}°F corresponde a {} °C:" .format (c, f))
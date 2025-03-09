#5) Crie um programa que converta uma temperatura de Celsius para Fahrenheit. O usuário
#deve inserir a temperatura em Celsius, e o programa deve exibir o equivalente em Fahrenheit.

c = float(input("Informe a temperatura em °C:"))
f = 9 * c / 5 + 32
print("A temperatura de {}°C corresponde a {} °F:" .format (c, f))
# 9. Contar quantos números pares o usuário digitar. O programa deve
# contar quantos números pares o usuário inseriu. O usuário para
# digitando -1.

numero = int(input("Digite um numero:"))
contador = 0
cont_pares = 0


while contador < numero:
  contador = contador +1
  if numero % 2 == 0:
    cont_pares = cont_pares + 1
  
print(f"Pares:", {cont_pares})
numero = int(input("Digite(-1 para sair:)"))

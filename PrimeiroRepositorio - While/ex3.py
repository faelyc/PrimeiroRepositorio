# 3 Somar números até o usuário digitar 0. Peça números ao usuário e
# some-os até que ele digite 0.

num = int(input("Digite um numero:"))
soma = 0

while num != 0:
  soma += num
  num = int(input("Digite um numero ou (zero para sair:)"))
print(soma)
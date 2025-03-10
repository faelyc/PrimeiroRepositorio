# 8. Encontrando o maior número inserido pelo usuário. Peça números ao
# usuário e, ao digitar 0, exiba o maior número inserido.

primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero: '))
terceiro = int(input('Terceiro numero: '))

   
maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('Maior: ',maior)

# 5. Some todos os números de 1 a 500 e mostre o resultado.


n = int(input('Digite um numero entre 1 e 500: '))
Soma = 0
while (n != 0):
    if n > 0:
     Soma += n
     n-=1

    else:
     Soma -= n
     n+=1    

print ('Soma = ', Soma)

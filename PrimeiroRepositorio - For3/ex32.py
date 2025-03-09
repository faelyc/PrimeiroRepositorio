# 32 Faça um programa que verifique e mostre os números entre 1.000 e 2.000
# que, quando divididos por 11 produzam resto igual a 2.



for num in range(1000,2000):
    if(num % 11 == 2):
        print (num)
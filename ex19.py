# 19 Crie uma lista com 6 itens e verifique se existe uma palavra dentro dela, utilizando o operador in. Depois, verifique uma palavra que não existe dentro dela utilizando o operador not in.

lista = ["casa", "carro", "mesa", "cadeira", "janela", "porta"]

palavra1 = input("Digite uma palavra para verificar na lista: ")
palavra2 = input("Digite uma palavra que não deve estar na lista: ")

print(f"A palavra '{palavra1}' está na lista?", palavra1 in lista)
print(f"A palavra '{palavra2}' NÃO está na lista?", palavra2 not in lista)
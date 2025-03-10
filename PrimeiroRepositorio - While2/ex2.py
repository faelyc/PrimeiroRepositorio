# 2. Solicite ao usuário que insira uma senha e continue pedindo até que ele insira a senha correta definida previamente.


senha = int(input("Digite uma senha: "))
senha_correta = 0



while senha != senha_correta:
    senha_correta = int(input("Digite a senha correta: "))

    if senha != senha_correta:
        print("Senha incorreta. Digite a senha correta.")
    
print("Senha correta.")
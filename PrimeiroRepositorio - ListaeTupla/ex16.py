# 16. Criar uma lista de nomes e exibir apenas os nomes que começam com a letra A.
nomes = ["Ana", "Bruno", "Alice", "Carlos", "Amanda", "Beatriz"]

nomes_a = [nome for nome in nomes if nome.startswith('A')]

print(nomes_a)
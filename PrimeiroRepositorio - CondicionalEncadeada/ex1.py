# 1 Escreva um programa que leia a nota de um aluno (de 0 a 100) e
# classifique-a como:
# • "A" se nota ≥ 90;
# • "B" se 80 ≤ nota < 90;
# • "C" se 70 ≤ nota < 80;
# • "D" se 60 ≤ nota < 70;
# • "F" se nota < 60.

nota = float(input("Digite a nota do aluno:"))

if nota >= 90:
  print("A")
elif nota >= 80 and nota <= 90:
  print("B")
elif nota >= 70 and nota <= 80:
  print("C")
elif nota >= 60 and nota <= 70:
  print("D")
else:
  print("F")
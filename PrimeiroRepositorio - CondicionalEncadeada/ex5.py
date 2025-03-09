# 5 Escreva um programa que leia a velocidade de um veículo e a
# classifique em:
# • "Baixa velocidade" para velocidades até 40 km/h;
# • "Velocidade moderada" para velocidades entre 41 e 80 km/h;

# • "Velocidade alta" para velocidades entre 81 e 120 km/h;
# • "Velocidade muito alta" para velocidades acima de 120 km/h.



velocidade = float(input("Insira a velocidade do veiculo:"))


if velocidade <=40:
  print("Baixa velocidade")
elif velocidade >=41 and velocidade <=80:
  print("Velocidade moderada")
elif velocidade >81 and velocidade <=120:
  print("Velocidade alta")
elif velocidade >120:
  print("velocidade muito alta")
#16
m=[[0 for i in range(4)] for i in range(3)]
mes=0
semana=0
ano=0
for i in range(3):
  for j in range(4):
    m[i][j]=int(input())
for i in range(3):
  for j in range(4):
      semana=m[i][j]
      mes+=semana
      print(f"Total da semana {i+1} do mês {i+1}: {semana}")
  ano+=mes
  print(f"Total do mês {i+1}: {mes}")
  mes=0
print(f"Total do ano: {ano}")
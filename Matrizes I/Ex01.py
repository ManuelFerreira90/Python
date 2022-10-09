#01
matriz=[[20 for i in range(5)]for i in range(5)]
for i in range(5):
  for j in range(5):
    matriz[i][j]=int(input())
for i in range(5):
  for j in range(4,3,-1):
    print(matriz[i][j])
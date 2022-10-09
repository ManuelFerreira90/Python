#02
matriz=[[20 for i in range(2)]for i in range(2)]
n=int(input())
c=0
for i in range(2):
  for j in range(2):
    matriz[i][j]=int(input())
for i in range(2):
  for j in range(2):
      if matriz[i][j] == n:
          print(f"matriz[{i}][{j}]={matriz[i][j]}")
          c+=1
if c==0:
  print("Error")
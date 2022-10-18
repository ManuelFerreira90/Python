#10
ma=[[0 for i in range(2)] for i in range(2)]
mb=[[0 for i in range(2)] for i in range(2)]
soma=0
for i in range(2):
  for j in range(2):
    ma[i][j]=int(input("Matriz A:"))
    mb[i][j]=int(input("Matriz B:"))
    soma+=ma[i][j]+mb[i][j]
print(soma)
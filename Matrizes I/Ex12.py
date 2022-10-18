#12
m=[[0 for i in range(3)] for i in range(2)]
soma=0
for i in range(2):
  for j in range(3):
    m[i][j]=int(input())
    soma+=m[i][j]
print(soma)
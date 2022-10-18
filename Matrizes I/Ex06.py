#06
m=[[0 for i in range(3)] for i in range(3)]
c=1
soma=0
for i in range(3):
  for j in range(3):
    m[i][j]=int(input())
for i in range(3):
  for j in range(0+c,3):
    soma+=m[i][j]
  c+=1
print(soma)
#13
m=[[0 for i in range(3)] for i in range(2)]
v=[0 for i in range(2)]
for i in range(2):
  for j in range(3):
    m[i][j]=int(input())
    v[i]+=m[i][j]
for i in range(2):
  print(v[i],end=" ")
#05
m=[[0 for i in range(4)] for i in range(4)]
c=1
for i in range(4):
  for j in range(4):
    m[i][j]=int(input())
for i in range(4):
  for j in range(0+c,4):
    print(m[i][j],end=" ")
  c+=1
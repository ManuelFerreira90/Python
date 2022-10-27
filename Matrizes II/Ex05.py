#05
m=[[0 for i in range(4)] for i in range(4)]
c=0
for i in range(4):
  for j in range(4):
    m[i][j]=int(input())
for i in range(3):
  for j in range(0,3-c):
    print(m[i][j],end='')
  c+=1
#08
m=[[0 for i in range(3)] for i in range(3)]
c=0
for i in range(3):
  for j in range(3):
    m[i][j]=int(input())
for i in range(1,3):
  for j in range(2-c,3,1):
    print(m[i][j])
  c+=1
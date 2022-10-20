#14
m=[[0 for i in range(3)] for i in range(2)]
x=0
for i in range(2):
  for j in range(3):
    m[i][j]=int(input())
for i in range(2):
  x=m[i][0]
  for j in range(3):
    if m[i][j]>x:
      x=m[i][j]
  print(x)
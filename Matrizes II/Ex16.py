#16
l=int(input())
c=int(input())
m=[[0 for i in range(c)] for i in range(l)]
mi=[[0 for i in range(l)] for i in range(c)]
for i in range(l):
  for j in range(c):
    m[i][j]=int(input())
for i in range(l):
  for j in range(c):
    mi[i][j]=-m[i][j]
for i in range(l):
  for j in range(c):
    print(mi[i][j],end="\t")
  print()
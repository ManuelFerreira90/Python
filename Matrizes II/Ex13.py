#13
l=int(input())
c=int(input())
m=[[0 for i in range(c)] for i in range(l)]
mt=[[0 for i in range(l)] for i in range(c)]
for i in range(l):
  for j in range(c):
    m[i][j]=int(input())
for i in range(c):
  for j in range(l):
    mt[i][j]=m[0+j][0+i]
for i in range(c):
  for j in range(l):
    print(mt[i][j],end="\t")
  print()
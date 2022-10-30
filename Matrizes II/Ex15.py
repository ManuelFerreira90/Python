#15
l=int(input())
c=int(input())
m=[[0 for i in range(c)] for i in range(l)]
mt=[[0 for i in range(l)] for i in range(c)]
t=False
cont=0
for i in range(l):
  for j in range(c):
    m[i][j]=int(input())
for i in range(c):
  for j in range(l):
    mt[i][j]=m[0+j][0+i]
for i in range(c):
  for j in range(l):
    if mt[i][j]==-m[i][j] or mt[i][j]==0:
      cont+=1
if cont==c*l:
    t=True
print("Antissímetrica:",t)
for i in range(c):
  for j in range(l):
    print(mt[i][j],end="\t")
  print()
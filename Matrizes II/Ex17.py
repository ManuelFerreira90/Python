#17
c=int(input("Linha 1º"))
d=int(input("Coluna 1º"))
e=int(input("Linha 2º"))
f=int(input("Coluna 2º"))
ma=[[0 for i in range(d)] for i in range(c)]
mb=[[0 for i in range(f)] for i in range(e)]
mc=[[0 for i in range(f)] for i in range(c)]
l=0
m1=0
for i in range(c):
  for j in range(d):
    ma[i][j]=int(input("1º"))
for i in range(e):
  for j in range(f):
    mb[i][j]=int(input("2º"))
if d==e:
    for b in range(f):
      for i in range(f):
        for j in range(d):
          mc[b][i]+=ma[b][j]*mb[j][i]


for i in range(c):
    for j in range(f):
      print(mc[i][j],end="\t")
    print()
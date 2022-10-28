#08
m=[[0 for i in range(10)] for i in range(10)]
mem=0
mem1=0
mem2=0
mem3=0
for i in range(10):
  for j in range(10):
    m[i][j]=int(input())
#troca
for j in range(10):
    mem=m[1][j]
    m[1][j]=m[7][j]
    m[7][j]=mem
for i in range(10):
  mem1=m[i][3]
  m[i][3]=m[i][9]
  m[i][9]=mem1
for i in range(10):
  for j in range(10):
    print(m[i][j],end="\t")
  print()
print()
for i in range(5):
  for j in range(5):
    mem2=m[i][0+j]
    m[i][0+j]=m[i][9-j]
    m[i][9-j]=mem2
for i in range(5,10):
  for j in range(5):
    mem3=m[i][4-j]
    m[i][4-j]=m[i][5+j]
    m[i][5+j]=mem3
#matriz final
for i in range(10):
  for j in range(10):
    print(m[i][j],end="\t")
  print()
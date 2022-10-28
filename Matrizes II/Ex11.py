#11
m=[[0 for i in range(3)] for i in range(3)]
m1=[[0 for i in range(3)] for i in range(3)]

for i in range(3):
  for j in range(3):
    m[i][j]=int(input())
for i in range(3):
  for j in range(3):
    m1[i][j]=m[0+j][2-i]
for i in range(3):
  for j in range(3):
    print(m1[i][j],end="\t")
  print()
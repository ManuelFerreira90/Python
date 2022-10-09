#03
m=[[0 for i in range(2)] for i in range(3)]
for i in range(3):
  for j in range(2):
    m[i][j]=int(input())
    if m[i][j]%2!=0:
      m[i][j]=m[i][j]*2
for i in range(3):
  for j in range(2):
    print(m[i][j],end="\t")
  print()
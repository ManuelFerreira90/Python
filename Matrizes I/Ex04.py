#04
m=[[0 for i in range(2)] for i in range(2)]
for i in range(2):
  for j in range(2):
    m[i][j]=int(input())
for i in range(2):
  for j in range(2):
    if i == j:
      print(m[i][j],end=" ")
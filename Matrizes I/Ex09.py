#09
ma=[[0 for i in range(2)] for i in range(3)]
mb=[[0 for i in range(2)] for i in range(3)]
for i in range(3):
  for j in range(2):
    ma[i][j]=int(input())
for i in range(3):
  for j in range(2):
    mb[i][j]=ma[i][j]*3
    print(mb[i][j],end="\t")
  print()
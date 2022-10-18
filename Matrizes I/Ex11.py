#11
ma=[[0 for i in range(2)] for i in range(2)]
mb=[[0 for i in range(2)] for i in range(2)]
m=[[0 for i in range(2)] for i in range(2)]
for i in range(2):
  for j in range(2):
    ma[i][j]=int(input("Matriz A:"))
    mb[i][j]=int(input("Matriz B:"))
    m[i][j]=ma[i][j]-mb[i][j]
for i in range(2):
  for j in range(2): 
    print(m[i][j],end="\t")
  print()
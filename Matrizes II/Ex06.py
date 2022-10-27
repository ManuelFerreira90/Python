#06
m=[[0 for i in range(4)] for i in range(2)]
for i in range(2):
  for j in range(3):
    m[i][j]=input()
    m[i][1]=int(m[i][1])
    m[i][2]=int(m[i][2])
    m[i][3]=int(m[i][3])
for i in range(2):
  for j in range(4):
    if j == 2:
      m[i][3]=m[i][1]-m[i][2]
      if m[i][3]>0:
        print(f"Nome: {m[i][0]} Precisa: {m[i][3]} ")
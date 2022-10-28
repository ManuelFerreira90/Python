#12
m=[[0 for i in range(2)] for i in range(2)]
det=0
diagonal1=1
diagonal2=1

for i in range(2):
  for j in range(2):
    m[i][j]=int(input())
for i in range(2):
  for j in range(2):
    if i==j:
      diagonal1*=m[i][j]
    if j==1-i:
      diagonal2*=m[i][j]
det=diagonal1-diagonal2
print(det)
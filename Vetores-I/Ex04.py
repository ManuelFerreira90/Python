#04
v=[0 for i in range(4)]
for i in range(4):
  v[i]=int(input())
  if i%2==0:
    v[i]=0
for i in range(4):
  print(v[i],end=" ")

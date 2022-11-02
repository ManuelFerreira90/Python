#13
v=[0 for i in range(5)]
m=0
for i in range(5):
  v[i]=int(input())
for i in range(5):
  for i in range(4):
    if v[i]>v[i+1]:
      m=v[i]
      v[i]=v[i+1]
      v[i+1]=m
for i in range(5):
  print(v[i],end=" ")
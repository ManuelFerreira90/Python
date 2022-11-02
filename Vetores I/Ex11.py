#11
v=[0 for i in range(5)]
for i in range(5):
  v[i]=int(input())
  if v[i]>=0:
    v[i]=v[i]**0.5
  else:
    v[i]=-1
for i in range(5):
  print(v[i],end=" ")
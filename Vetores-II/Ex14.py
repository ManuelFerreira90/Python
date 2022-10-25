#14
v=[0 for i in range(4)]
v1=[0 for i in range(4)]
m=0
for i in range(4):
  v[i]=int(input())
  v1[i]=v[i]
for i in range(4):
  for j in range(4):
    if v[i]<v[j]:
      m=v[i]
      v[i]=v[j]
      v[j]=m
    if v1[i]>v1[j]:
      m=v1[i]
      v1[i]=v1[j]
      v1[j]=m
for i in range(4):
  print(v[i],end=" ")
print()
for i in range(4):
  print(v1[i],end=" ")
    
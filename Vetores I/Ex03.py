#03
v=[0 for i in range(5)]
m=0
c=0
for i in range(5):
  v[i]=int(input())
for i in range(2):
  m=v[i]
  v[i]=v[4-c]
  v[4-c]=m
  c+=1
for i in range(5):
  print(v[i],end=" ")
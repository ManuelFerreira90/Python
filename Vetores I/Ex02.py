#02
v=[0 for i in range(5)]
a=int(input())
for i in range(5):
  v[i]=int(input())
for i in range(5):
  if v[i]<a:
    print(v[i],end=" ")
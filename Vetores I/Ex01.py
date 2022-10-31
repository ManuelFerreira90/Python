#01
a=int(input())
v=[0 for i in range(5)]
for i in range(5):
  v[i]= int(input())
for i in range(5):
  v[i]=v[i]*a
  print(v[i],end=" ")
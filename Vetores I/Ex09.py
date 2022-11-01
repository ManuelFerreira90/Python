#09
v=[0 for i in range(5)]
va=[0 for i in range(5)]
vb=[0 for i in range(5)]
for i in range(5):
  v[i],va[i]=map(int,input().split(" "))
for i in range(5):
  vb[i]=v[i]+va[i]
  print(vb[i],end=" ")
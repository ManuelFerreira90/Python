#08
v1=[0 for i in range(4)]
v2=[0 for i in range(4)]
m=0
c=0
for i in range(4):
  v1[i]=int(input())
for i in range(4):
  v2[i]=v1[3-c]
  c+=1
  print(v2[i])
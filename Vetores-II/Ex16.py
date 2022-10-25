#16
v=[0 for i in range(4)]
soma=0
u=0
p=0
for i in range(4):
  v[i]=int(input())
for i in range(2):
  soma+=(v[0+p]-v[3-u])**3
  u+=1
  p+=1 
print(soma)      
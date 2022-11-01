#06
n=int(input())
v=[0 for i in range(n)]
soma=0
for i in range(n):
  v[i]=int(input())
for i in range(n):
  if i%2==0:
    soma+=v[i]
print(soma)
#desafio
n=int(input())
v=[0 for i in range(n)]
vn=[]
m=0
c=0
tm=0
for i in range(n):
  v[i]=int(input())
for i in range(n):
  for i in range(n-1):
    if v[i]>v[i+1]:
      m=v[i]
      v[i]=v[i+1]
      v[i+1]=m
for i in range(n):
  for j in range(i+1,n):
    if v[i]==v[j]:
      c+=1
  if c<1:
    vn.append(v[i])
    tm+=1
  c=0
#vr=[0 for i in range(len(vn))]
for i in range(tm):
  for j in range(n):
    if vn[i]==v[j]:
      c+=1
  print(f'{vn[i]} aparece {c} vez(es)')
  c=0
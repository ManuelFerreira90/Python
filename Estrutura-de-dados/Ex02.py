#02
n=int(input("Tamanho vetor: "))
n1=int(input("Tamanho vetor1: "))
v=[0 for i in range(n)]
v1=[0 for i in range(n1)]
v2=[0 for i in range(n+n1)]
c=0
m=0
for i in range(n):
  v[i]=int(input())
for i in range(n1):
  v1[i]=int(input())
for i in range(n+n1):
  if n<n1:
    if i%2==0 and c<n:
        v2[i]=v[c]
        c+=1
    else:
      v2[i]=v1[m]
      m+=1
  elif n1<n:
    if i%2==0 and c<n1:
        v2[i]=v1[c]
        c+=1
    else:
      v2[i]=v[m]
      m+=1
  else:
      if i%2==0:
        v2[i]=v[c]
        c+=1
      else:
        v2[i]=v1[m]
        m+=1
print(v2)
#16
n=int(input("Digite a quantidade de valores nos dois vetores: "))
v=[0 for i in range(n*2)]
va=[0 for i in range(n)]
vb=[0 for i in range(n)]
c1=0
c2=1
for i in range(n):
  va[i]=int(input())
  vb[i]=int(input())
for i in range(n):
  v[i+c1]=va[i]
  v[i+c2]=vb[i]
  c1+=1
  c2+=1
for i in range(n*2):
  print(v[i],end=" ")
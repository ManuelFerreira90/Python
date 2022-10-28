#07
n=int(input())
crM=0
c='a'
c1=0
c2=0
c3=0
nn='a'
n1=0
n2=0
n3=0
p=0
m=[[0 for i in range(4)] for i in range(n)]
for i in range(n):
  v=int(input())
  sexo=int(input())
  cr=int(input())
  c1=(((v%10**8)%10**7)%10**6)//10**5
  c2=((((v%10**8)%10**7)%10**6)%10**5)//10**4
  c3=(((((v%10**8)%10**7)%10**6)%10**5)%10**4)//10**3
  n1=((((((v%10**8)%10**7)%10**6)%10**5)%10**4)%10**3)//10**2
  n2=(((((((v%10**8)%10**7)%10**6)%10**5)%10**4)%10**3)%10**2)//10**1
  n3=(((((((v%10**8)%10**7)%10**6)%10**5)%10**4)%10**3)%10**2)%10**1
  c1=str(c1)
  c2=str(c2)
  c3=str(c3)
  n1=str(n1)
  n2=str(n2)
  n3=str(n3)
  c=c1+c2+c3
  nn=n1+n2+n3
  m[i][0]=c
  m[i][1]=sexo
  m[i][2]=cr
  m[i][3]=nn
  if i==0:
    crM=cr
  if m[i][2]>crM:
     crM=m[i][2]
     p=i
m[p][2]=crM
print(f"Matricula: {m[p][3]} cr: {m[p][2]} Codigo: {m[p][0]}")

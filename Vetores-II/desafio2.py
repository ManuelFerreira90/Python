#desafio 02
n=int(input())
v=[0 for i in range(n)]
vn=[]
m=0
c=0
tm=0
aux=0
pos=0
for i in range(n):
  v[i]=int(input())
for i in range(n):
  for j in range(i+1,n):
    if v[i]==v[j]:
      c+=1
  if c<1:
    vn.append(v[i])
    tm+=1
  c=0
vc=[0 for i in range(tm)]
for i in range(tm):
  for j in range(n):
    if vn[i]==v[j]:
      vc[i]+=1
comparar=vc[0]
vc1=[]   
for i in range(tm):
  if vc[i]>comparar:
    comparar=vc[i]
for i in range(tm):
  if vc[i]==comparar:
    aux+=1
    pos=i
if aux==1:
  print("Número que repete mais vezes:",vn[pos])
else:
  for i in range(tm):
    if vc[i]==comparar:
      vc1.append(vn[i])
  comparar2=vc1[0]
  for i in range(len(vc1)):
    if vc1[i]>comparar2:
      comparar2=vc1[i]
  print("Maior número que repete mais vezes:",comparar2)
print(comparar)
print(vc)
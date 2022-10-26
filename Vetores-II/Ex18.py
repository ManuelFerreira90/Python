#18
vt=[0 for i in range(5)]
vi=[0 for i in range(5)]
m=0
c=0
for i in range(5):
  vt[i]=int(input())
  vi[i]=vt[i]
for i in range(5):
  for i in range(4):
    if vt[i]>vt[i+1]:
      m=vt[i]
      vt[i]=vt[i+1]
      vt[i+1]=m

  
for i in range(5):
  for j in range(5):
    if vt[i]==vi[j]:
      print(f"{i+1}º coloado é o competidor {j} com o tempo de {vt[i]}")
  c+=1

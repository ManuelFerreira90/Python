#16
nome='Thor'
nomenovo=''
nome1=''
v=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
v1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#contador
b=0
p=0
m=1
a=0
g=0
for i in nome:
    for j in range(26):
      if i==v[j] or i==v1[j]:
        nomenovo+=v1[j]
    p+=1
#conferir
print(nomenovo)
#saída
for y in range(p):
  for z in range(g,m):
      nome1+=nomenovo[z]
      print(nome1)
  if m==4:
      break
  m+=1
  g+=1
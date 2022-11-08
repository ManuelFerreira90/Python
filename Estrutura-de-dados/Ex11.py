#11
frase=str(input())
#contador
c=1
tm=0
for i in frase:
  tm+=1
  if i==" ":
    c+=1
if frase[tm-1]==" ":
  c=c-1
if frase[0]==' ':
  c=c-1
print(c)
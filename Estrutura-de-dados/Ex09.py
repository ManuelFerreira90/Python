#09
frase="Quem parte e reparte fica com a maior parte"
strvelha="parte"
strnova="parcela"
v=0
#contador
c=0
l=0
b=0
a=0
pos=0
pos1=0
for i in frase:
  if i==strvelha[b]:
    c+=1
    b+=1
    if b==5:
      pos1=a+1
    if i==strvelha[4]:
      pos2=a
    if b==5:
      b=0
  elif i!=strvelha[b]:
      c=0
      b=0
  if c==5:
      l+=1
  a+=1
v=frase[0:pos1-5]
v+=strnova
if frase[pos2]>="a" or frase[pos2]>="A":
  v+=frase[pos2+1:a]
print(v)
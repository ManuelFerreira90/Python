#15
frase=str(input())
frase=frase.lower()
frase=list(frase)
frase2=str(input())
frase2=frase2.lower()
frase2=list(frase)
c1=0
c2=0
c3=0
m1=''
m2=''
anagrama=False
for i in frase:
  c1+=1
for i in frase2:
  c2+=1
if c1==c2:
  for i in range(c1):
    for i in range(c1-1):
      if frase[i]>frase[i+1]:
        m1=frase[i]
        frase[i]=frase[i+1]
        frase[i+1]=m1
      if frase2[i]>frase2[i+1]:
         m2=frase2[i]
         frase2[i]=frase2[i+1]
         frase2[i+1]=m2
  for i in range(c1):
    if frase[i]==frase2[i]:
        c3+=1
    if c3==c1:
      anagrama=True
print(frase)
print(frase2)
print("True é um anagrama, False não é um anagrama")
print(anagrama)
#13
frase1=str(input())
frase2=str(input())
l=True
#contador
c=0
p=0
m=False
for i in frase1:
  c+=1
for i in frase2:
  p+=1
if c==p:
  for i in frase1:
      if i==frase2[c-1]:
        m=True
        c-=1
      else:
        m=False
  print("É um palíndromo")
else:
  print("Não é um palíndromo")
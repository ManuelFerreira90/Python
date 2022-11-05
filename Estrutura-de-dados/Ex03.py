#03
v=[0.0 for i in range(4)]
media=0
c=0
menor=0
comparar=0
valor=0
for i in range(4):
  v[i]=float(input())
  media+=v[i]
  c+=1
media=media/c
if v[0]>media:
  menor=v[0]-media
  valor=v[0]
else:
  menor=media-v[0]
for i in range(1,4):
  if media>v[i]:
    comparar=media-v[i]
    if comparar<menor:
      menor=comparar
      valor=v[i]
  else:
    comparar=v[i]-media
    if comparar<menor:
      menor=comparar
      valor=v[i]
print(valor)
#09
v=[0 for i in range(4)]
Mt=0
mt=0
medt=0
tmm=0
for i in range(4):
  v[i]=int(input())
Mt=v[0]
mt=v[0]  
for i in range(4):
  medt+=v[i]
  if v[i]>Mt:
    Mt=v[i]
  if v[i]<mt:
    mt=v[i]
medt=medt/4
for i in range(4):
  if v[i]<medi:
    tmm+=1
print("Menor temperatura:",mt)
print("Maior temperatura:",Mt)
print("Medias das temperatura:",medt)
print("Numero de dias que a temperatura foi menor que a media",tmm)
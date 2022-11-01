#10
v=[0 for i in range(5)]
vn=["a" for i in range(5)]
mn=0
Mn=0
nM="A"
nm="a"
for i in range(5):
  v[i]=int(input())
  vn[i]=str(input())
mn=v[0]
Mn=v[0]
for i in range(5):
  if v[i]>Mn:
    Mn=v[i]
    nM=vn[i]
  if v[i]<mn:
    mn=v[i]
    nm=vn[i]
print(f"Maior nota: {Mn} aluno: {nM}")
print(f"Menor nota: {mn} aluno: {nm}")
#05
m=[[0 for i in range(2)] for i in range(4)]
nomecarro='a'
kmporl=0
for i in range(4):
  for j in range(1):
    m[i][0],m[i][1]=input().split(' ')
    m[i][1]=float(m[i][1])
nomecarro=m[0][0]
kmporl=m[0][1]
for i in range(4):
  if m[i][1]<kmporl:
    kmporl=m[i][1]
    nomecarro=m[i][0]
print('Carro mais econômico: ',nomecarro)
for i in range(4):
  print(f'Modelo: {m[i][0]}, Gasta: {(1000/m[i][1])*3.5} para percorrer 1000 Km')
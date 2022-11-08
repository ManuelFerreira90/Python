#05
m=[[0 for i in range(2)] for i in range(4)]
nomecarro='a'
kmporl=0
for i in range(4):
  for j in range(1):
    m[i][0],m[i][1]=input().split(" ")
    m[i][1]=float(m[i][1])   
for i in range(4):
  for i in range(3):
    if m[i][1]>m[i+1][1]:
        nomecarro=m[i][0]
        kmporl=m[i][1]
        m[i][0]=m[i+1][0]
        m[i][1]=m[i+1][1]
        m[i+1][0]=nomecarro
        m[i+1][1]=kmporl
print("Carro mais econômico: ",m[0][0])
for i in range(4):
  for j in range(1):
    print(f"Modelo: {m[i][j]},  Gasto: {m[i][j+1]*3.5}")
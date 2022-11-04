#18
va=[]
vs=[]
#índice
i=0
id=0
saldototal=0
clienteN=0
c=0
while id>=0:
  v.append(int(input("Digite o nº da conta: ")))
  id=v[i]
  if id>=0:
    vs.append(int(input("Digite o saldo da conta: ")))
    saldototal+=vs[i]
    if vs[i]<0:
      clienteN+=1
  else:
    break
  c+=1
  i+=1
for i in range(c):
  if vs[i]<0:
    print(f"Nº da conta {v[i]} Saldo: {vs[i]} Negativo")
  else:
    print(f"Nº da conta {v[i]} Saldo: {vs[i]} Positivo")
clienteN=(clienteN*100)/c
print("Saldo total da agência: ",saldototal)
print("Total de clientes: ",c)
print("Total de pessoas negativadas: ",clienteN)
print("% de pessoas negativados: ",clienteN)
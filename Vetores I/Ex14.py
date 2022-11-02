#14
v=[]
vp=[]
valortotal=0
#índice
i=0
id=0
while id>=0:
  v.append(int(input("Digite seu id: ")))
  id=v[i]
  if id>=0:
    vp.append(int(input("Digite o valor à pagar: ")))
    valortotal+=vp[i]
  else:
    break
  i+=1
print("Valor total à pagar: ",valortotal)
#17
v=[0 for i in range(5)]
vn=["a" for i in range(5)]
vd=[0 for i in range(5)]
for i in range(5):
  vn[i]=str(input("Digite o nome da mercadoria: "))
  v[i]=float(input("Digite o valor da mercadoria: "))
  vd[i]=v[i]*5.15
for i in range(5):
  print(f"Nome da mercadoria: {vn[i]} valor em reais{v[i]} em dólar {(vd[i])}  ")
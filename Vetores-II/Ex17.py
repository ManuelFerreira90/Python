#17
vp=[0 for i in range(4)]
vq=[0 for i in range(4)]
faturamento=0.0
for i in range(4):
  vp[i]=float(input("Digite o preço da mercadoria: "))
  vq[i]=int(input("Quantidade vendida: "))
for i in range(4):
  faturamento+=vp[i]*vq[i]
print(f"Faturamento mensal R$ {faturamento}")

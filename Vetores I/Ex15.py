#15
n=int(input("Digite a quantidade de caixas descarregadas: "))
vt=int(input("Digite o valor monetário total da carga: "))
v=[0 for i in range(n)]
vp=[0 for i in range(n)]
vt2=0
p=0
for i in range(n):
  v[i]=int(input(f"Digite o peso da caixa {i}: "))
  vp[i]=int(input(f"Digite o preço da caixa {i}: "))
  vt2+=vp[i]
  p+=v[i]
print("Peso total após a descarga: ",p)
if vt2!=vt:
  print("Conflito entre valores")
else:
  print("Valor está correto") 
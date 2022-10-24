#10
n=int(input())
medren=0
medianaren=0
u=0
v=[0 for i in range(n)]
for i in range(n):
  v[i]=float(input("Digite a renda: "))
for i in range(n):
  medren+=v[i]
if n%2==0:
  u=((n//2)+((n//2)+1))/2
  medianaren=u
  print("Mediana: ",medianaren)
else:
  u=(n//2)
  medianaren=v[u]
  print("Mediana: ",medianaren)
print("Media salario: ", medren/n)
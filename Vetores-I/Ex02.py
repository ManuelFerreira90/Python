#02
v=[0 for i in range(20)]
menor=0
maior=0
for i in range(20):
  v[i]=int(input())
menor=v[0]
maior=v[0]
for i in range(20):
  if v[i] < menor:
    menor=v[i]
  if v[i] > maior:
    maior=v[i]
print("Maior: ",maior)
print("Menor: ",menor)
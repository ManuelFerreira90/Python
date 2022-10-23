#03
v=[0 for i in range(20)]
menor=0
maior=0
for i in range(3):
  v[i]=int(input())
menor=v[0]
maior=v[0]
for i in range(3):
  if v[i] < menor:
    menor=v[i]
  if v[i] > maior:
    maior=v[i]
for i in range(3):
  if v[i] == maior:
      print(f"v[{i}] {maior}")
  if v[i] == menor:
      print(f"v[{i}] {menor}")
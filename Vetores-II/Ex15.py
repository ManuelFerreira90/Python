#15
v=[0 for i in range(4)]
vnr=[-1 for i in range(4)]
for i in range(4):
  v[i]=int(input())
for i in range(4):
  for j in range(4):
    if v[i] == v[j]:
      vnr[i]+=1
for i in range(4):
  print(f"Número: {v[i]} Vezes repetido: {vnr[i]}")
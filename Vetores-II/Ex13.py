#13
va=[0 for i in range(4)]
vb=[0 for i in range(4)]
x=int(input())
for i in range(4):
  va[i]=int(input("A"))
  vb[i]=int(input("B"))
for i in range(4): 
  if va[i] == x:
    print(f"Posicao do vb correspondente a posicao va[i] = x: {vb[i]}")
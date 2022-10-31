#04
v=[0 for i in range(5)]
n=int(input())
c=0
for i in range(5):
  v[i]=int(input())
for i in range(5):
  if v[i] == n:
    print(f"Posição {i}")
    c+=1
if c==0:
  print("Error")
#19
n=[0 for i in range(4)]
a=0
d=0
m=0
for i in range(4):
  n[i]=int(input())
a=n[3]
for i in range(4):
  for i in range(3):
    if n[i]>n[i+1]:
      m=n[i]
      n[i]=n[i+1]
      n[i+1]=m
d=n[3]
for i in range(4):
  print(n[i],end=" ")
print()
print("K-ésimo termo antes da ordenação: ",a)
print("K-ésimo termo depois da ordenação: ",d)
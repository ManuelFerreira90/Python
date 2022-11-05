#01
import random
v=[0 for i in range(10)]
maior=0
c=0
for i in range(10):
  v[i]=random.randrange(1,10)
  if i==0:
    maior=v[0]
  if v[i]>maior:
    maior=v[i]
v1=[0 for i in range(maior)]
for i in range(maior):
  v1[i]=i+1
  for j in range(10):
    if v1[i]==v[j]:
      c+=1
  v1[i]=c
  c=0
print(v)
print()
print(v1)
#desafio
n=int(input())
t=input().split(' ')
l=0
for i in range(n):
  t[i]=int(t[i])
  if i==0:
    menor=t[i]
    l=i+1
  if t[i]<menor:
    menor=t[i]
    l=i+1
print(l)
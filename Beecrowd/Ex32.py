#02
n=int(input())
x=input().split(' ')
menor=0
posicao=0
for i in range(n):
    x[i]=int(x[i])
menor=x[0]
for i in range(n):
    if x[i]<menor:
        menor=x[i]
for i in range(n):
    if x[i]==menor:
        break
print("Menor valor:",menor)
print("Posicao:",i)
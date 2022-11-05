
#01
vetor=[0 for i in range(5)]
a=int(input())
mult=0

for i in range(5):
    vetor[i]=int(input())
for i in range(5):
    mult=a*vetor[i]
    if(mult%2==0):
         print(f"{mult} é par")
    else:
         print(f"{mult} é ímpar")
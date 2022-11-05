#02
vetor=[0 for i in range(5)]
menor=0
for i in range(5):
    vetor[i]=int(input())
menor=vetor[0]
for i in range(5):
    if(vetor[i]<menor):
         menor=vetor[i]
print(menor)
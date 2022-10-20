#02
import random
import os
listan=['raquer','rildo','tarop']
listas=['ferreira','jack','gabriel']
n=int(input())
arquivo=input()
arq=open(arquivo, 'w')
for i in range(n):
  arq.write(listan[i])
  arq.write(' ')
  arq.write(listas[i])
  arq.write(' ')
  arq.write(str(random.randrange(1,100)))
  arq.write(' ')
  arq.write('\n')
arq.close()
print(os.getcwd)
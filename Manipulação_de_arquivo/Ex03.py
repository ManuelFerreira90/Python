#03
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
  arq.write('idade: ')
  arq.write(str(random.randrange(1,100)))
  arq.write(' ')
  arq.write('altura: ')
  arq.write(str(round(random.uniform(1.1,2.0),2)))
  arq.write('\n')
arq.close()
print(os.getcwd)
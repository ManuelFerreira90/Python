#01
import os
arquivo=input()
arq=open(arquivo, 'w')
for i in range(200,49,-1):
  arq.write(str(i))
  arq.write("\n")
arq.close()
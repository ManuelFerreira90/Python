#04
arq1=input()
arq2=input()
arquivo1=open(arq1, 'r')
arquivo2=open(arq2, 'w')
for i in arquivo1:
  arquivo2.write(str(i))
arquivo2.close()
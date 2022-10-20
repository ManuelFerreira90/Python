#05
arq1=input()
arq2=input()
arq3=input()
arquivo1=open(arq1, 'r')
arquivo2=open(arq2, 'r')
arquivo3=open(arq3, 'w')
listano=arquivo2.readlines()
listanom=arquivo1.readlines()
nota=''
media=0
nome=[0 for i in range(4)]
notas=['' for i in range(4)]
qtd=0
j=0
for i in range(4):
    nome[i]=listanom[i]
for i in range(4):
    if listano[i]!=' ' and listano[i]!='\n':
        nota+=listano[i]
        media+=int(nota)
    elif listano=='\n':
        media=media/3
        notas[i]=str(media)
        media=0

print(nome)
print(notas)
#06
m=[]
n=0
nome=0
nome1=0
telefone=0
nome2='a'
telefone='a'
nome3='a'
#contador
c=0
l=0
while n!=2:
  n=int(input("Digite 0 para adicionar um número: ""\n""Digite 1 para procurar um telefone:  ""\n""Digite 2 para encerrar o programa: ""\n"))
  if n==0:
    nome2=str(input("Nome: "))
    telefone2=str(input("Telefone: "))
    m.append([nome2,telefone2])
    c+=1
    #odenação 
    if c>=2:
      for i in range(c):
        for i in range(c-1):
          if m[i][0]>m[i+1][0]:
            nome1=m[i][0]
            telefone=m[i][1]
            m[i][0]=m[i+1][0]
            m[i][1]=m[i+1][1]
            m[i+1][0]=nome1
            m[i+1][1]=telefone
  elif n==1:
    nome=str(input('Digite o nome que deseja saber o número: '))
    l=1
    for i in range(c):
      if nome<=m[i][0]:
        if nome==m[i][0]:
          nome3=m[i][1]
          print(f"Número da/o que você procurou: {nome3}")
          l=0  
    if l==1:
        print("Nome não encontrado!")
  else:
    for i in range(c):
      for j in range(2):
        print(m[i][j],end=" ")
      print()
    break
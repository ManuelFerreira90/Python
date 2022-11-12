#17
mes=[['de janeiro de'],['de fevereiro de'],['de março de'],['de abril de'],['de maio de'],['de junho de'],['de julho de'],['de agosto de'],['de setembro de'],['de outrubro de'],['de novembro de'],['de dezembro de']]
data=str(input('Digite uma data: '))
novadata=''
mes1=data[3]+data[4]
mes1=int(mes1)
mes2=mes[mes1-1]
#contador
c=0
p=0
a=0

for i in data:
  if p<=2:
    if i!='/':
        novadata+=i
    else:
        novadata+=' '
  elif p==3:
      for b in mes2:
        novadata+=b
  elif p>=5:
    if i!='/':
        novadata+=i
    else:
        novadata+=' '
  p+=1
print(novadata)
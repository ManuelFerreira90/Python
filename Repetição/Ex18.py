#18
n1=37
n2=38
n3=1
resultado=0
for i in range(37):
    resultado += (n1*n2)/n3
    n1-=1
    n2-=1
    n3+=1
print(resultado)
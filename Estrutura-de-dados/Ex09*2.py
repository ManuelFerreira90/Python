#09
frase=input()
strvelha=input()
strnova=input()
retirar=frase.rsplit(strvelha,1)
frase=strnova.join(retirar)
print(frase)
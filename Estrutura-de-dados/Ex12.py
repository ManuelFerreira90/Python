#12
frase=str(input())
frasenova=''
c=0
for i in frase:
    if i!=" ":
      frasenova+=i
    else:
      frasenova+='#'
print(frasenova)
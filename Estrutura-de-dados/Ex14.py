#14
frase=str(input())
frasenova=''
v=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
v1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#contador
c=-1
l=0
for i in frase:
  c+=1
for i in range(c,-1,-1):
    for j in range(26):
      if frase[i]==v[j] or frase[i]==v1[j]:  
        frasenova+=v1[j]
print(frasenova)
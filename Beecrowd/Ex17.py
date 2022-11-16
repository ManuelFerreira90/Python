#03
nome = "a"
distfinal = 0
contador = 0
guardardist = 0
while nome != "EOF":
    nome = str(input())
    if(nome != "EOF"):
        dist = int(input())
        guardardist += dist
        contador += 1
distfinal = guardardist/contador
print("%.1f"%distfinal)

#03
distfinal = 0
contador = 0
guardardist = 0
while True:
    try:
        nome = str(input())
        dist = int(input())
        guardardist += dist
        contador += 1
    except:
        distfinal = guardardist / contador
        print("%.1f"%distfinal)
        break
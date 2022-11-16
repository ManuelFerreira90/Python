#05
w1 = 1
w2 = 1
r = 1
contador = 0
guardarm = 0
mfinal = 0
m = 0
while w1 !=0 and w2 !=0 and r!=0:
    w1,w2,r = map(int,input().split(" "))
    if w1 !=0 and w2 !=0 and r!=0:
        m = ((w1*(1+(r/30))) + (w2*(1+(r/30)))) / 2
        if m >= 1 and m < 13:
                print("Nao vai da nao")
                guardarm += m
                contador += 1
        elif m >= 13 and m < 14:
                print("E 13")
                guardarm += m
                contador += 1
        elif m >= 14 and m < 40:
                print("Bora, hora do show! BIIR!")
                guardarm += m
                contador += 1
        elif m >= 40 and m <= 60:
                print("Ta saindo da jaula o monstro!")
                guardarm += m
                contador += 1
        elif m > 60:
                print("AQUI E BODYBUILDER!!")
                guardarm += m
                contador += 1
    else:
        mfinal = guardarm / contador
        if mfinal > 40:
            print("\n""Aqui nois constroi fibra rapaz! Nao e agua com musculo!")
        break
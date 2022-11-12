#Tempo de Jogo
a, b = map(int, input().split(" "))

if (a >= b):
    m = (24 - a) + b
    print("O JOGO DUROU",m,"HORA(S)")
else:
    m = b - a
    print("O JOGO DUROU",m,"HORA(S)")

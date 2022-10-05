#14
c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0
pb = 0
pn = 0
for i in range(0,5):
    a = int(input())
    if a == 1:
       c1 = c1 + 1
    elif a == 2:
        c2 = c2 + 1
    elif a == 3:
        c3 = c3 + 1
    elif a == 4:
        c4 = c4 + 1
    elif a == 5:
        vn = vn + 1
    elif a == 6:
        vb = vb + 1
    pb = ((c1 + c2 + c3 + c4) * vb) / 100
    pn = ((c1 + c2 + c3 + c4) * vn) / 100

print("O total de votos candidato 1= ",c1)
print("O total de votos candidato 2= ",c2)
print("O total de votos candidato 3= ",c3)
print("O total de votos candidato 4= ",c4)
print("O total de votos nulos = ",vn)
print("O total de votos brancos= ",vb)
print("Percentual de votos brancos= ",pb)
print("Percentual de votos nulos= ",pn)


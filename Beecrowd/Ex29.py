#04
O=str(input())
valor=0
media=0
c=0
v=0
matriz=[[0 for i in range(12)] for i in range(12)]
for i in range(0,12):
    for j in range(0,12):
        matriz[i][j]=float(input())
for i in range(1,6):
    for j in range(11,10-c,-1):
        if O == "S" or O == "M":
            valor+=matriz[i][j]
    c+=1
for i in range(6,11):
    for j in range(7+v,12):
        if O == "S" or O == "M":
            valor+=matriz[i][j]            
    v+=1
if O == "M":
    media=valor/66
    print("%.1f"%media)
elif O == "S":
    print(valor)
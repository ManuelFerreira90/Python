#14
a1 = int(input())
a2 = int(input())
n = int(input())
apar = 0
aimpar = 0
for i in range(1,(n+1)):
    if i % 2 != 0:
        aimpar += a1 + a2
        print(a1,a2, end = " ")
        a1 = a2
        a2 = aimpar 
    else:
        apar += a1 - a2
        print(a1,a2, end = " ")
        a1 = a2
        a2 = apar
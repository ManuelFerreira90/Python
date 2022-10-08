#15
n1,n2,n3,n4,n5,n6,n7,n8,n9,n10 = map(int,input().split(" "))
dentro = 0
fora = -1

for i in range(10,21):
    if(n1 == i or n2 == i or n3 == i or n4 == i or n5 == i or n6 == i or n7 == i or n8 == i or n9 == i or n10 == i):
        dentro += 1
    else:
        fora += 1    
print("Quantidade de números dentro do intevalo: ",dentro)
print("Quantidade de números fora do intevalo: ",fora)
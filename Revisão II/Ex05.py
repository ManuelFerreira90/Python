#05
num = int(input())

for i in range(1,(num+1)):
    if(i % 3 == 0 and i % 5 == 0):
          print("É múltiplo de 3 e 5:", i)
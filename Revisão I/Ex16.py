#16
for i in range(1,6):
    a, b = map(int,input().split(" "))
    for i in range(a, (b+1)):
        if(i % 2 == 0):
          print(i, end=" ")
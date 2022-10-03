#09
b = 0
num = 1
l = 0
while num != -1:
    num = int(input())
    if num != -1:
        for i in range(1):
            b = b + num
            l = l + 1 
    else:
        print(b / l)
        break
#4
m = 1
n = 1
while m > 0 and n > 0:
    sum = 0
    num = 0
    m, n = map(int,input().split(" "))
    if m <= 0 or n <= 0:
        break
    else:
        num = [m,n]
        num.sort()   
        for i in range(num[0], num[1]+1):
            sum = sum + i
            print(i, end = " ")
        print(f"Sum={sum}")
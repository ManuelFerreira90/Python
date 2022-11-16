#01
n = int(input())
n1 = 1
n2 = 0
n3 = 0

for i in range(1,(n)):
    print(n3, end = " ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print(n3)
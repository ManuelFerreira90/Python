#02
s = 1
n1 = 3
n2 = 2
for i in range(1,19):
    s += n1/n2
    n1 += 2
    n2 *= 2

print("%.2f"%s)
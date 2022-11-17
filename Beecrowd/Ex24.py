#04
n = [0 for i in range(20)]
c = 0
memoria = 0
for i in range(20):
    n[i] = int(input())
for i in range(10):
    memoria = n[i]
    n[i] = n[19-c]
    n[19-c] = memoria
    c += 1
for i in range(20):
    print(f"N[{i}] = {n[i]}")
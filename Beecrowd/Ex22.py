#02
n = [1 for i in range(11)]
n[0] = int(input())
for i in range(10):
    n[i+1] = n[i] * 2
    print(f"N[{i}] = {n[i]}")
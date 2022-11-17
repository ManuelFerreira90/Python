#03
a = [0 for i in range(100)]
for i in range(100):
    a[i] = float(input())
for i in range(100):
    if a[i] <= 10:
        print(f"A[{i}] = {a[i]}")
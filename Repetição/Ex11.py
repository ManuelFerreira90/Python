#11
m = 0
for i in range(1,3):
    n = int(input("Digite um número: "))
    if n != 0:
        for l in range(1, n + 1):
            m = l * n
            print(f"{l}x{n}={m}")
#05
v = int(input())
for i in range(v):
    x = int(input())
    fib = [0 for i in range(x+2)]
    fib[0]=0
    fib[1]=1
    for i in range(2,(x+1)):
        fib[i]=fib[i-1]+fib[i-2]
    print(f"Fib({x}) = {fib[x]}")
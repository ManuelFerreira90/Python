#05
n=1
c=0
while n!=0:
    n=int(input())
    if n!=0:
        matriz=[[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                matriz[i][j]=2**(j+c)
            c+=1
        c=0
        T = len(str(matriz[n-1][n-1]))
        for i in range(n):
            for j in range(n):
                matriz[i][j] = str(matriz[i][j])
        for i in range(n):
            for j in range(n):
                while len(matriz[i][j]) < T:
                    matriz[i][j] = " " + matriz[i][j]
            M = " ".join(matriz[i])
            print(M)
        print()
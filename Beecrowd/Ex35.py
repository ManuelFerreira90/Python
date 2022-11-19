#05
c=0
while True:
    try:
        n=int(input())
        m=[[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i+j == n-1 :
                    m[i][j]=2
                elif i == j:
                    m[i][j] = 1
                else:
                    m[i][j]=3
                print(m[i][j],end="")
            print()
            c+=1
    except EOFError:
        break
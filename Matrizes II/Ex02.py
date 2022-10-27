#02
m=[[0 for i in range(3)]for i in range(3)]
c=0
for i in range(3):
    for j in range(3):
        m[i][j]=int(input())
for i in range(3):
    for j in range(0,c):
            print(m[i][j],end=" ")
    c+=1
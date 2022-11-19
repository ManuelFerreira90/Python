#03
N=str(input())
m=[[0.0 for i in range(12)]for i in range(12)]
c=0
l=0
somaoumedia=0.0
for i in range(12):
    for j in range(12):
        m[i][j]=float(input())
for i in range(0,5):
    for j in range(1+c,11-c):
        if N == "S":
            somaoumedia+=m[i][j]
        elif N == "M":
            somaoumedia+=m[i][j]
            l+=1
    c+=1
if N == "M":
    somaoumedia=somaoumedia/l
    print("%.1f"%somaoumedia)
elif N == "S":
    print("%.1f"%somaoumedia)

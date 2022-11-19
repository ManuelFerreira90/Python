#01
vp = [0 for i in range(5)]
vi = [0 for i in range(5)]
par=0
impar=0
for i in range(3):
    for j in range(5):
        n=int(input())
        if n%2==0:
            vp[par]=n
            par+=1
        else:
            vi[impar]=n
            impar+=1
        if impar==5:
            for c in range(5):
                print(f"impar{[c]} = {vi[c]}")
                impar=0
        if par==5:
            for a in range(5):
                print(f"par{[a]} = {vp[a]}")
                par=0
        if i == 2 and j == 4:
            for c in range(impar):
                print(f"impar{[c]} = {vi[c]}")
            for a in range(par):
                print(f"par{[a]} = {vp[a]}")
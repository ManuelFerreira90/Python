#04
c = int(input())
for i in range(1,(c+1)):
    nome, forca = input().split(" ")
    nome = str(nome)
    forca = int(forca)
    if nome == "Thor":
        print("Y")
    else:
        print("N")
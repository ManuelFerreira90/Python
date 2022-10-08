#17
termo1 = int(input("Digite o primeiro termo para a serie RICCI: "))
termo2 = int(input("Digite o segundo termo para a serie RICCI: "))
N = int(input("Digite até qual termo quer da sério de RICCI: "))
termo3 = 0

print(termo1)
print(termo2)
for i in range(1,(N+1)):
    termo3 = termo1 + termo2
    print(termo3)
    termo1 = termo2 
    termo2 = termo3
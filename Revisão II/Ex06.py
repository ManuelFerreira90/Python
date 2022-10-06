#06
quantidade = 0 

for i in range(1,16):
    numeros = float(input())
    if numeros > 30:
        quantidade += 1

print(f"Foram digitados {quantidade} números maiores que 30")        
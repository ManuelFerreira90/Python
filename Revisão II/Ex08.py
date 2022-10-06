#08
n = 1
maior = 0
menor = 0

while n != -1:
    n = int(input())
    if n != -1:
        for i in range(n):
            if n > maior:
                maior = n
            if i == 0:
                menor = i
            if i < menor:
                menor = i            
    else:
      break

print("Maior número:",maior)
print("Menor número:",menor)
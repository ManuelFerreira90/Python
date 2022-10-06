#07
n = 1
contador = 0
media = 0
l = 0
while n > 0:
    n = int(input())
    if n > 0:
        if n % 3 == 0:
           contador += 1
           #l irá receber a soma de n
           l += n
    else:
      break
media = l / contador

print("A média dos múltiplos de 3 é :",media)

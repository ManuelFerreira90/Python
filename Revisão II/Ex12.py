#12
x = float(input())
senox = 0
e = -1
denominador = 1
expoente = 1
l = 1

rad = (x * 3.14) / 180

for i in range(1,16):
      #variável e faz com que a cada repetição a fração seja
      #positiva e na próxima negativa
      e *= -1
      senox += ((rad ** expoente) / denominador) * e
      denominador = 1
      expoente += 2
      l += 2
      for j in range(1,(l+1)):
          denominador *= j
print(" O seno de",x,"é igual a %.1f"%senox)
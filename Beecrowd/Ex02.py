#Triângulo
A, B, C = map(float, input().split(" "))

if A + B > C and A + C > B and C + B > A:
    perimetro = A + B + C
    print("Perimetro = %.1f"%(perimetro))
else:
    areatrapezio = (((A + B) * C) / 2)
    print("Area = %.1f"%(areatrapezio))
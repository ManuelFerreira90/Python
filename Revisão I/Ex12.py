#12
nota1 = float(input())
nota2 = float(input())

medianotas = (nota1 + nota2) / 2

if medianotas >= 7:
    print("Aprovado")
elif medianotas < 3:
    print("Reprovado")
else:
    print("Exame") 
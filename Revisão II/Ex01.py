#01
peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

if imc < 20:
    print("Abaixo do peso")
elif imc >= 20 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obeso")
else:
    print("Obeso Mórbido")
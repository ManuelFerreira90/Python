#01
a = int(input("Digite o valor gasto no restaurante: "))
gorjeta = 0
Valortotal = 0

gorjeta = (a * 10) / 100
valortotal = a + gorjeta

print("Valor da gorjeta: R$", gorjeta)
print("Valor total com a gorjeta: R$",valortotal)
#02
x = float(input())

if(x > 2000.00):
    if( x <= 3000.00):
        salario = x - 2000.00
        imposto = salario * 0.08
        print("R$ %.2f"%(imposto))
    elif( x > 3000.00 and x <= 4500.00):
        salario = x - 3000.00
        imposto = salario * 0.18 + 80.00
        print("R$ %.2f"%(imposto))
    elif( x > 4500.00):
        salario = x - 4500.00
        imposto =  (salario * 0.28) + 350
        print("R$ %.2f"%(imposto))
else:
    print("Isento")
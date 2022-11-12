#Aumento de Salário
s = float(input())

if s >= 0 and s <= 400.00:
    r = s * 0.15
    s = r + s
    print("Novo salario: %.2f"%(s))
    print("Reajuste ganho: %.2f" %(r)) 
    print("Em percentual: 15 %")
elif s >= 400.01 and s <= 800.00:
    r = s * 0.12
    s = r + s
    print("Novo salario: %.2f"%(s))
    print("Reajuste ganho: %.2f" %(r)) 
    print("Em percentual: 12 %")
elif s >= 800.01 and s <= 1200.00:
    r = s * 0.10
    s = r + s
    print("Novo salario: %.2f"%(s))
    print("Reajuste ganho: %.2f" %(r)) 
    print("Em percentual: 10 %")
elif s >= 1200.01 and s <= 2000.00:
    r = s * 0.07
    s = r + s
    print("Novo salario: %.2f"%(s))
    print("Reajuste ganho: %.2f" %(r)) 
    print("Em percentual: 7 %")
elif s > 2000.00:
    r = s * 0.04
    s = r + s
    print("Novo salario: %.2f"%(s))
    print("Reajuste ganho: %.2f" %(r)) 
    print("Em percentual: 4 %")
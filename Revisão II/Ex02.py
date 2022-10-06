#02
saldomedio = float(input())

if saldomedio >=0 and saldomedio <= 500:
    print("Saldo médio = " ,saldomedio )
    print("Nenhum crédito")
elif saldomedio > 500 and saldomedio <= 1000:
    valorcredito = saldomedio * 0.30
    print("Saldo médio = ", saldomedio )
    print("Valor do crédito  = %.2f" %(valorcredito))
elif saldomedio > 1000 and saldomedio <= 3000:
    valorcredito = saldomedio * 0.40
    print("Saldo médio = ", saldomedio )
    print("Valor do crédito = %.2f" %(valorcredito))
elif saldomedio > 3000:
    valorcredito = saldomedio * 0.50
    print("Saldo médio = ", saldomedio )
    print("Valor do crédito = %.2f" %(valorcredito))
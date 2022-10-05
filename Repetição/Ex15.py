#15
nome = str(input())
cv = int(input())
vt = float(input())
s = 500.00

cv = cv * 50
vt = ((vt * 5)/100)
print(f"{nome} recebeu R$ {cv+vt+s}")
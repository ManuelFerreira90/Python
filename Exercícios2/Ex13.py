#13
n = int(input())

if n % 3 == 0 and n % 7 == 0:
   print("É divisível por 3 e 7")
elif n % 3 == 0:
   print("É divisível por 3")
elif n % 7 == 0:
   print("É divisível por 7")
else:
   print("Não é divisível por 3 nem por 7")
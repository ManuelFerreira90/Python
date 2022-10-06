#09
raiz = 0

for i in range(1,11):
    n = int(input())
    if n >= 0:
      raiz = n ** 0.5
      print(f"Raiz de {n} = {raiz}")
    else:
      break
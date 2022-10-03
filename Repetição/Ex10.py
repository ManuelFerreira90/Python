#10
a = int(input())
n = 1

if a < 0:
  print("Fatorial não existe")
else:
  for i in range(1, a + 1):
     n = n * i
  print(f"{a}! = {n}")
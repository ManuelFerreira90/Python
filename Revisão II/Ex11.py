#11
a = int(input())
b = int(input())
mod = a

while mod >= 0:
      if mod - b > 0:
          mod = mod - b
      else:
         break

print("Mod de A / B =", mod)
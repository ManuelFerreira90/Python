#19
natalidadeA = 5000000
natalidadeB = 7000000
contadoranos = 0
while natalidadeA <= natalidadeB:
    if natalidadeA <= natalidadeB:
        natalidadeA += 5000000 * 0.03
        natalidadeB += 7000000 * 0.02
        contadoranos += 1
    else:
      break
print(f"Necessários {contadoranos} anos")

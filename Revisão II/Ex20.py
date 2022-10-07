#20
cicliA = 10
cicliB = 15
distanciaA = 0
distanciaB = 0
distancia = 2000
tempo = 0
while distancia > 0:
    if distancia > 0:
        distancia -= cicliA + cicliB
        distanciaA += 10
        distanciaB += 15
        tempo += 1
    else:
      break
print(f"Levou {tempo} segundos")
print(f"Distância ciclista A: {distanciaA} metros")
print(f"Distância ciclista B: {distanciaB} metros")
#16
masc = 0
fem = 0
sim = 0
nao = 0
pfs = 0
pmn = 0

for i in range(1,5):
  sexo = int(input())
  voto = int(input())
  if sexo == 1:
    masc += 1
  else:
    fem += 1
  if voto == 1:
    sim += 1
  else:
    nao += 1
pfs = (((masc + fem) * sim) / 100)
pmn = (((masc + fem) * nao) / 100)
print("O número de pessoas que responderam sim", sim)
print("O número de pessoas que responderam não", nao)
print("A porcentagem de pessoas do sexo feminino que responderam sim", pfs)
print("A porcentagem de pessoas do sexo masculino que responderam não", pmn)
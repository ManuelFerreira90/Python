#12
vn=[0 for i in range(10)]
vfa=[-1 for i in range(10)]
vfr=[0 for i in range(10)]
c=0
for i in range(10):
  vn[i]=int(input())
for i in range(10):
  for j in range(10):
    if vn[i] == vn[j]:
        vfa[i]+=1
  vfr[i]=vfa[i]/10
for i in range(10):
  print(f"Nota do {i} aluno: {vn[i]}")
  print(f"Frequência absoluta: {vfa[i]}")
  print(f"Frequência relativa: {vfr[i]}")
  print()

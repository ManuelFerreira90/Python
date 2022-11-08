#10
dna=str(input())
dna2=""
for i in dna:
    if i=="A":
      dna2+="T"
    elif i=="T":
      dna2+="A"
    elif i=="C":
      dna2+="G"
    elif i=="G":
      dna2+="C"
print(dna2)
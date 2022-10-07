#15
otimo = 0
bom = 0
regular = 0
ruim = 0
pessimo = 0
contidade = 0
idadepessimo = 0
idadeotimo = 0
idaderuim = 0
mediaidaderuim = 0

for i in range(1,5):
    idade = int(input("Digite sua idade: "))
    opfilme = str(input("Qual sua opinião sobre o filme" "\n" "A = Ótimo" "\n" "B = Bom" "\n" "C = Regular" "\n" "D = Ruim" "\n" "E = Péssimo""\n")) 
    if opfilme == "A":
        otimo += 1
        if idade > idadeotimo:
             idadeotimo = idade
    elif opfilme == "B":
        bom += 1
    elif opfilme == "C":
        regular += 1
    elif opfilme == "D":
        ruim += 1
        idaderuim += idade
        contidade +=1
        if idade > idaderuim:
            idaderuim = idade
    elif opfilme == "E":
        pessimo += 1
        if idade > idadepessimo:
             idadepessimo = idade
total = otimo + bom + regular + ruim + pessimo
percentualBeD = ((bom * 100) / total) - ((regular * 100) / total)
if contidade > 0:
    mediaidaderuim = idaderuim / contidade
else:
    mediaidaderuim = "Ninguem votou em ruim"
porcenpessimo = (pessimo * 100) / total
print(f"Responderam ótimo {otimo} pessoas")
print(f"A diferença percentual bom e regular %{percentualBeD}")
print("A média de idade votou ruim: ",mediaidaderuim)
print(f"A porcentagem péssimo : {porcenpessimo} e a maior idadeque votou: {idadepessimo}",)
print("a diferença de idade maior entre ótimo e ruim: ",idadeotimo)
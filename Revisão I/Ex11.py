#11
destino = str(input("Digite seu destino: "))
idaevolta = str(input("Sua viagem é ida e volta sim ou não: "))

if idaevolta == "sim":
    if destino == "Região Norte":
        print("O valor da sua passagem é de R$900,00")
    if destino == "Região Nordeste":
        print("O valor da sua passagem é de R$650,00")
    if destino == "Região Centro-Oeste":
        print("O valor da sua passagem é de R$600,00")
    if destino == "Região Sul":
        print("O valor da sua passagem é de R$550,00")
else:
    if destino == "Região Norte":
        print("O valor da sua passagem é de R$500,00")
    if destino == "Região Nordeste":
        print("O valor da sua passagem é de R$350,00")
    if destino == "Região Centro-Oeste":
        print("O valor da sua passagem é de R$350,00")
    if destino == "Região Sul":
        print("O valor da sua passagem é de R$300,00")

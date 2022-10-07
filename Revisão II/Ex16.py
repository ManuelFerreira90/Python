#16
nome = "a"
alturamaior = 0
pesomaior = 0
mediaidade = 0
contador = 0
receberaidade = 0
nomeatletaMmaior = "a"
nomeatletaFpeso = "a"

while nome != "@":
    nome = str(input("Digite seu nome: "))
    if nome != "@":
        sexo = str(input("Digite seu sexo M ou F: "))
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        contador += 1
        receberaidade += idade
        if sexo == "M":
            if altura > alturamaior:
                alturamaior = altura
                nomeatletaMmaior = nome
        if sexo == "F":
            if peso > pesomaior:
                pesomaior = peso
                nomeatletaFpeso = nome

    else:
        break
mediaidade = receberaidade / contador
print(f"Atleta masculino mais alto, nome: {nomeatletaMmaior} altura: {alturamaior} ")
print(f"Atleta feminina  mais pesada, nome: {nomeatletaFpeso} peso: {pesomaior}")
print("A média de idade dos atletas:",mediaidade)
#17
numeropedido = 1
valortotal = 0
while numeropedido != 0:
        numeropedido = int(input("Digite o número do pedido: "))
        if numeropedido != 0:
            datadopedido = int(input("Digite a data do pedido dia, mês e ano: "))
            Preçounitario = float(input("Digite o valor do produto: "))
            quantidadeproduto = int(input("Digite a quantidade de produtos: "))
            valortotal += quantidadeproduto * Preçounitario
        else:
            break
print("Valor total da compra R$",valortotal)
#18
vetorconta=[]
vetorsaldo=[]
vetorpessn=[]
conta=1
c=0
contsaldon=0
saldoagen=0
porcen=0
while conta>=0:
  vetorconta.append(int(input()))
  conta=vetorconta[c]
  if conta>=0:
    vetorsaldo.append(int(input()))
    saldoagen+=vetorsaldo[c]
    if vetorsaldo[c]>=0:
      print(f"Conta: {vetorconta[c]} Saldo: {vetorsaldo[c]} P")
    elif vetorsaldo[c]<0:
      contsaldon+=1
      print(f"Conta: {vetorconta[c]} Saldo: {vetorsaldo[c]} N")
  else:
    break
  c+=1
porcen=(contsaldon*100)/c
print("Total de clientes: ",c)
print("Total de clientes negativados:",contsaldon)
print("Saldo da agencia: ",saldoagen)
print("Porcentagem de pessoas negativadas: ",porcen)
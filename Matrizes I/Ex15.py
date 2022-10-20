#15
n=int(input("Digite o número de funcionários: "))
m=[[0 for i in range(3)] for i in range(n)]
salario=0.0
for i in range(n):
  for j in range(3):
    m[i][j]=float(input())
for i in range(n):
  for j in range(3):
    if m[i][0]:
        salario=m[i][0] * 10
    if m[i][1]:
        salario=(m[i][1] * 15)+ salario
    if m[i][2]:
        salario=(m[i][2] * 30)+ salario
  print(f"Salário do {i+1}º funcionário R${salario*0.5}")
  salario=0
#03
nM = 0
nm = 0
for n in range(5):
    n1 = int(input())
    if n1 > nM:
       nM = n1
    if n == 1:
        nm = n1
    if n1 < nm:
        nm = n1
print("O maior número digitado foi: ",nM)
print("O menor número digitado foi: ",nm)
#20
x=int(input())
r=0
e=-1

for i in range(1,26):
    e*=-1
    r+=(((x**(26-i))/i)*e)
print(r)
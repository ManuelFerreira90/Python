#1
a = int(input())

h = a // 100
h2 = (a % 100) // 50
h3 = ((a % 100) % 50) // 20
h4 = (((a % 100) % 50) % 20) // 10
h5 = ((((a % 100)% 50) % 20) % 10) // 5
h6 = (((((a % 100) % 50) % 20) % 10)% 5) // 2
h7 = (((((a % 100) % 50 % 20) % 10) % 5) % 2) // 1

print(a)
print(h,"nota(s) de R$ 100,00")
print(h2,"nota(s) de R$ 50,00")
print(h3,"nota(s) de R$ 20,00")
print(h4,"nota(s) de R$ 10,00")
print(h5,"nota(s) de R$ 5,00")
print(h6,"nota(s) de R$ 2,00")
print(h7,"nota(s) de R$ 1,00")
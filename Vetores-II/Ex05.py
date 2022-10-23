#05
v=[0 for i in range(4)]
c=0
b=0
for i in range(4):
  v[i]=int(input())
for i in range(4):
    for j in range(1,v[i]+1):
       if v[i] // j == 1 or v[i] // j == v[i]:
          c+=1
          if c == 2:
            print(f"v[{i}] {v[i]}")
    b=0
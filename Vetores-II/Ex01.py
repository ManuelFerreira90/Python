#01
v=[0 for i in range(10)]
media=0
for i in range(10):
  v[i]=int(input())
for i in range(10):
  media+=v[i]
print(media/10)
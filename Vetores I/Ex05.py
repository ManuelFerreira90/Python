#05
v=[0 for i in range(5)]
media=0
for i in range(5):
  v[i]=int(input())
for i in range(5):
  media+=v[i]
print(media/5)
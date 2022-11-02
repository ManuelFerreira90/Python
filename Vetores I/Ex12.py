#12
v=[0 for i in range(5)]
media=0
for i in range(5):
  v[i]=int(input())
  media+=v[i]
media=media/5
for i in range(5):
  if v[i]>media:
    print(v[i],end=" ")
#07
v=[0 for i in range(21)]
for i in range(21):
  if i%2!=0:
    v[i]=i**2
  else:
    v[i]=i
for i in range(21):
  print(v[i])
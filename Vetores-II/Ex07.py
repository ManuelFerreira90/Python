#07
v=[0 for i in range(4)]
mp=0
mi=0
medp=0
medi=0
cp=0
ci=0
for i in range(4):
  v[i]=int(input())
mp=v[0]
mi=v[0]  
for i in range(4):
  if v[i]%2==0:
      medp+=v[i]
      cp+=1
      if v[i]>mp:
       mp=v[i]
  if v[i]%2!=0:
     medi+=v[i]
     ci+=1
     if v[i]<mi:
       mi=v[i]
medp=medp/cp
medi=medi/ci
for i in range(4):
  if v[i]%2==0:
      if v[i]>medp:
        print("Valor par maior que a media:",v[i]) 
  if v[i]%2!=0:
      if v[i]<medi:
        print("Valor impar menor que a media:",v[i])
print("Media par: ",medp)
print("Media impar: ",medi)
  
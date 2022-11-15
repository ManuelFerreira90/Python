l,a,p,r=map(int,input().split(" "))

d=((l**2+a**2+p**2)**0.5)

if(r*2>=d):
   print("S")
else:
   print("N")
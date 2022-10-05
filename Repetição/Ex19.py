#19
n1=1
n2=1
s=0
pi=0
e=-1

for i in range(1,52):
   e*=-1
   s+=((n1/(n2**3))*e)
   n2+=2
   pi = ((s*32)**(1/3))
   print(pi)
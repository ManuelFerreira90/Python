#04
pa,pg,qa,qg = map(float, input().split(" "))

al = qa/pa
ga = qg/pg

if al > ga:
   print("A")
else:
   print("G")
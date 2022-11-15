#03
t1,t2,t3 = map(int,input().split(" "))

if((t1>=-100 and t1 <=100) and (t2>=-100 and t2<=100) and (t3>=-100 and t3<=100)):
    if(t1>t2 and t3>=t2):
        print(":)")
    elif(t2>t1 and t3<=t2):
        print(":(")
    elif(t2>t1 and t3>t2):
        if((t2 - t1) > (t3 - t2)):
             print(":(")
        elif((t2 - t1) <= (t3 -t2)):
          print(":)")
    elif(t1>t2 and t2>t3):
        if((t1 - t2) > (t2 - t3)):
            print(":)")
        elif((t1 - t2) <= (t2 - t3)):
            print(":(")
    elif(t1 == t2):
        if(t3>t2):
            print(":)")
        elif(t2>=t3):
             print(":(")
def aval(a,b):
    for i in range(a,b+1):
        if(i==1):
            continue
        elif(i==2):
            print(i)
            continue
        else:
            count=0
            for j in range(1,i+1):
                if(i%j==0):
                    count=count+1
            if(count<=2):
                print(i)
a=int(input())
b=int(input())
if(a<1 or a>10000 or b<1 or b>10000):
    print("Error")
else:
    if(a>=b):
        aval(b,a)
    else:
        aval(a,b)

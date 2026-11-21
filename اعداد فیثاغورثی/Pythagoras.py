def is_Pythagoras(a,b,c):
    if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
        print("YES")
    else:
        print("NO")
a=int(input())
b=int(input())
c=int(input())
is_Pythagoras(a,b,c)

def ShowFibNth(fibo_n,fibo_n1):
    result=fibo_n
    while(fibo_n1!=1): 
        print(result)
        result=fibo_n1-fibo_n
        fibo_n1=fibo_n
        fibo_n=result
    print(1)

    

first=1
second=1
fibo_n=int(input())
fibo_n1=int(input())
if(fibo_n>1000000 or fibo_n1>1000000):
    print("Error")
else:
    ShowFibNth(fibo_n,fibo_n1)

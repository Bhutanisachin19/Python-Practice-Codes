def Fib(prod):
    a=-1;b=1
    for i in range(0,prod):
        c=a+b
        print(c)
        a=b
        b=c

Fib(10)
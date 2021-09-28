def productFib(prod):
    a = -1 ; b = 1
    z = int(prod/3)
    if(prod == 0):
        l = [0,1,True]
        return l
    elif(prod==1):
        m = [1,1,True]
        return m
    elif(prod == 2):
        n =[1,2,True]
        return n
    elif(prod == 3 or prod==4):
        o = [2,3,False]
        return o
    else:
        for i in range(0,prod):
            for j in range(0,z):
                c = a+b 
                #print(c)
                a = b
                b = c
                if prod == (b*a):
                    mylist = [a,b,True]
                    return mylist
                elif prod < (a*b):
                    mylistt = [a,b,False]
                    return mylistt
                else:
                    pass
       




check = productFib(4)
print(check)


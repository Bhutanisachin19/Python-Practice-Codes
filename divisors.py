#divisiors

"""
example

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"


import array

def divisors(integer):
    a = array.array('i', []) 
    if(integer > 1):
        num = int(integer/2)

        for i in range(2,num+1):
            if(integer % i == 0):
                a.append(i)
        
        mylist = a.tolist()
        if(len(a) < 1):
            return ("{} is prime".format(integer))
        else:
            return(mylist)
                

"""

#same code without array


def divisors(integer):
    a =[]
    if(integer > 1):
        num = int(integer/2)

        for i in range(2,num+1):
            if(integer % i == 0):
                a.append(i)
        
        #mylist = a.tolist()
        if(len(a) < 1):
            return ("{} is prime".format(integer))
        else:
            return(a)
                

ans = divisors(20)

print(ans)

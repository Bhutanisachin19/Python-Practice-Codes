#hacker rank

"""
9
10 20 20 10 10 30 50 10 20


output 
3
"""



def sockMerchant(n, ar):
    mydict = {}

    for i in range(0,n):
        mydict = {ar[i]:ar.count(i)}

    print(mydict)


ar = [10 ,20, 20, 10, 10 ,30, 50, 10, 20]
sockMerchant(9,ar)
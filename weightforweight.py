import operator

def order_weight(strng):
    # your code
    my_dict = {}
    mylist = strng.split(" ")

    for i in range(0,len(mylist)):
        mylist[i] = int(mylist[i])

    #print(mylist)

    for i in range(0,len(mylist)):
        total = 0
        num = mylist[i]
        while(num > 0):
            remainder = num % 10
            num = int(num/10)
            total = total + remainder
        
        #creating dictionary
        my_dict.update({mylist[i]:total})
        #print(total)
    
    
    #explanation of this line
    sorted_d = sorted(my_dict.items(), key=operator.itemgetter(1))
    sorted_d = dict(sorted_d)

    #print(my_dict)
    #print(sorted_d)
    
    s = list(sorted_d.keys())
    listToStr = ' '.join(map(str, s)) 
    
    return listToStr

final = order_weight("56 65 74 100 99 68 86 180 90")
print(final)
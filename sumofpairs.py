
"""
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
"""

def sum_pairs(ints, s):
    coutnt = 0
    list2 = 0
    list1 = 0
    for i in range(0,len(ints)):
        for j in range(i+1,len(ints)):
                if (ints[i] + ints[j] ==s) and coutnt==0:
                    list1 = j
                    mylist = [ints[i],ints[j]]
                    coutnt = coutnt + 1
                    #return mylist
                else:
                    if ints[i] + ints[j] == s:
                        list2 = j
                        mylist2 = [ints[i],ints[j]]
    
     
    if list1 and list2 > 0:
        if list1 > list2:
            return mylist2
        else:
            return mylist
    elif list1 > 0:
        return mylist
    else:
        return None


    """
    print(mylist)
    print(mylist2)   
    """

l1= [20, -13, 40]
val = sum_pairs(l1, -7)
print(val)


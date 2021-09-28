#it should remove all values from list a, which are present in list b.

def array_diff(a, b):
    for i in b:
        while(i in a):
            a.remove(i)
        else:
            pass
    return a



mylist = array_diff([1,2,2,2,3],[2])
print(mylist)
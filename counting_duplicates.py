


def duplicate_count(text):
    text = text.lower()
    mylist = list(text)
    myset = set(text)
    countt = 0
    val = 0
    for i in myset:
        countt = mylist.count(i)
        if countt > 1:
            val = val +1
            countt = 0
        #print(i)
    
    #return val
    print(val)



duplicate_count("AABB")
#print(val)
     
#hackerrank
"""
def appendAndDelete(s,t,k):
    same = 0
    diff_s = 0
    diff_t = 0
    len_s = len(s)
    len_t = len(t)

    for i in t:
        if i in s:
            s = s.replace(i , "")
            same = same +1
        else:
            break

    print(same)
    print(s)

    diff_s = len_s - same 
    print(diff_s)

    diff_t = len_t - same
    print(diff_t)

    if(diff_s + diff_t <= k):
        print("YES")
    else:
        print("No")


appendAndDelete("abcd" , "abcdert",10)
"""





#Logic 2

def appendAndDelete(s,t,k):
    same = 0
    diff_s = 0
    diff_t = 0
    len_s = len(s)
    len_t = len(t)
    

    for i,j in zip(s,t):
        if i == j:
            same+=1
        else:
            break

    diff_s = len_s - same
    diff_t = len_t - same
    
    print(same)
    if((diff_s + diff_t) > k):
        print("No")
    elif((len_s + len_t) <= k):
        print("Yes")
    elif((k - len_s - len_t + 2 * same) % 2 == 0): 
        print ("Yes")
    else:
        print("No")



appendAndDelete("qwerasdf","qwerbsdf",6)
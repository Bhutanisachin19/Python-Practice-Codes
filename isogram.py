# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#to check whether an alphabet is repeated or not

def is_isogram(s):
    s1 = s.lower()
    for i in s1:
        a = s1.count(i)
        if(a > 1):
            res = False
            break
        else:
            res = True
    print(res)
 


is_isogram("mOose")


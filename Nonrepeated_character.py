def first_non_repeating_letter(string):
    #num = 0
        
    if len(string) == 0:
        return string
    s = string.lower()
    #print(s)
    for i in range(0,len(s)):
        num = 0
        num = s.count(s[i])
        #print(s[i])
        if(num == 1):
            return(string[i])
            break
    return ""
            


val = first_non_repeating_letter("")
print(val)
def duplicate_count(text):
    text=text.lower()
    for i in range(0, len(text)):
        count = 1
        for j in range(i+1, len(text)):
            if(text[i] == text[j] and text[i] != ' '):
                count =count + 1
                #Set string[j] to 0 to avoid printing visited character
                text = text[:j] + '0' + text[j+1:]
                #print(text)
        if(count > 1 and text[i] != '0'):
            return count


a = duplicate_count("aabBcde")
print(a)

"""
text = "abcdefaad";  

text= text.lower()
for i in range(0, len(text)):  
    count = 1
    for j in range(i+1, len(text)):  
        if(text[i] == text[j] and text[i] != ' '):  
            count = count + 1
            #Set string[j] to 0 to avoid printing visited character  
            text = text[:j] + '0' + text[j+1:]
   
    #A character is considered as duplicate if count is greater than 1  
    if(count > 1 and text[i] != '0'):  
        print(text[i]+" number of time it appear is {}" .format(count))
"""
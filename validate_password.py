"""


incomplete


The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore

"""

def alphanumeric(password):

    strength = False

    if len(password) <=0 :
        return False
    elif password.count("_") > 0:
        return False    
    elif password.count(" ") > 0:
        return False
    else:
        for i in range(0,len(password)):
            try:
                digits = int(password[i])
                print(digits)
                strength = True
            except:
                pass


    return strength



ans = alphanumeric("nQNld48T0gNVHzRJ	LAyI")
print(ans)
    
#leet code

"""
Input: -123
Output: -321

Input: 120
Output: 21
"""

def reverse(x):
    rev_no = 0
    negative = False

    if(x < 0):
        negative = True
        x = -(x) 

    while(x > 0 ):
        remainder = x % 10
        rev_no = (rev_no * 10) + remainder
        #x = x/10
        #print(x)
        x = x//10

    if(negative):
        return -rev_no
    else:
        return rev_no    


ans = reverse(120)
print(ans)
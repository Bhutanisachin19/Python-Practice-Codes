#Hacker Rank ,  valleys

def count_valley():
    #s = "DDUUDDUDUUUD"
    s="UDDDUDUU"
    valley = 0
    step = 0
    for i in range(0,len(s)):
        up = s.count("U")
        down = s.count("D")
        if s[i] == 'D':
            step = step - 1
        elif s[i] == 'U':
            step = step + 1
            if step == 0:
                valley = valley + 1
                print(valley)
    
    """
    print(up)
    print(down)
    print(valley)
    """

count_valley()
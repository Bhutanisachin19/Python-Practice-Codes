# to calculate last digit of a num when number and its power is given

def last_digit(n1, n2):
    if n2==0:
        return 1

    s = str(n1)
    s = s[-1]
    #last digit of a given number
    last_dig = int(s[0])

    if last_dig ==1 or last_dig == 5 or last_dig==6:
        return last_dig
    elif last_dig==0:
        return 0
    else:
        if last_dig==2:
            val = n2%4
            if val==0:
                return 6
            else:
                val = 2**val
                return int(val)
        elif last_dig==3:
            val = n2%4
            if val==0:
                return 1
            else:
                val = str(3**val)
                val = val[-1]
                return int(val)
        elif last_dig==4:
            val = n2%2
            if val==0:
                return 6
            else:
                val = str(4**val)
                val = val[-1]
                return int(val)
        elif last_dig==7:
            val = n2%4
            if val==0:
                return 1
            else:
                val = str(7**val)
                val = val[-1]
                return int(val)
        elif last_dig==8:
            val = n2%4
            if val==0:
                return 6
            else:
                val = str(8**val)
                val = val[-1]
                return int(val)
        elif last_dig==9:
            val = n2%2
            if val==0:
                return 1
            else:
                val = str(9**val)
                val = val[-1]
                return int(val)
        else:
            pass

    

val = last_digit(13,7)
print(val)
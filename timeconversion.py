#hackerrank

def timeConversion(s):
    num = 0
    if("PM" in s):
        time  = s.split(":")
        num = int(time[0])
        
        if(num < 12):
            num = num + 12
        
        time[0] = str(num)
        st = ":".join(time)
        st = st[:-2]
        return(st)
    
    if("AM" in s and "12" in s):
        time  = s.split(":")
        print(time)
        num = int(time[0])
        print(num)
        if num == 12:
            num = str('00')
            print(num)
            time[0] = num
            st = ":".join(time)
            #st = st[:-2]
            return(st)
    
    s = s[:-2]
    return(s)
            
            
converted = timeConversion('12:45:54PM')
print(converted)
     
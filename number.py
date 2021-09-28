#  1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


def narcissistic( value ):
    num = value
    val = str(value)
    digits = len(val)
    result = 0

    for i in range(0,digits):
        remainder = int(value % 10)
        #print(remainder)
        result += remainder ** digits
        #print(result)
        value = int(value / 10)
        #print(value)

    #print("Final Result")
    if result == num :
        return True
    else:
        return False



res = narcissistic(1634)
print(res)
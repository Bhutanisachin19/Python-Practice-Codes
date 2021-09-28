def solution(number):
    sum = 0
    #n = int(number)
    for i in range(number):
        if i % 3==0 and i % 5==0:
           # print("{} is a multiple of Both".format(i))
            sum=sum+i
        elif i % 5==0:
            #print("{} is a multiple of 5 ".format(i))
            sum=sum+i
        elif i % 3==0:
            #print("{} is a multiple of 3".format(i))
            sum=sum+i
        else:
            pass

    print("Sum is {}".format(sum))


solution(10)
def find_uniq(arr):
    num = arr[0]
    for i in range(1,len(arr)-1):
        if(arr[i]==num and arr[i+1]==num):
            pass
        else:
            if(arr[i]==num):
                n=arr[i+1]
            elif(arr[i+1]==num):
                n=arr[i]
            else:
                n=num
    # your code here
    return n   # n: unique integer in the array


num = find_uniq([0, 0, 0.55, 0, 0 ])
print(num)
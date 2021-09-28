
#Hacker Rank

def divisibleSumPairs(n, k, ar):

    small_list = []
    output = []
    for i in range(0,n):
        for j in range(i+1,n):
            if i < j and (ar[i] + ar[j] == k or (ar[i] + ar[j]) % k == 0) :
                small_list = [ar[i] , ar[j]]
                output.append(small_list)

    print(len(output))




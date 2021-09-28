
#hacker rank

def breakingRecords(scores):
    highest_num = 0
    lowest_num = 0
    high_count = 0 
    low_count = 0

    for i in range(0,len(scores)):
        if i == 0:
            highest_num = lowest_num = scores[0]
        
        if scores[i] < lowest_num:
            lowest_num = scores[i]
            low_count = low_count + 1

        if scores[i] > highest_num:
            highest_num = scores[i]
            high_count = high_count + 1
        
    
    print(high_count)
    print(low_count)



breakingRecords([10 ,5, 20, 20, 4 ,5 ,2, 25, 1])
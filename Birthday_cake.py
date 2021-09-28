#hackerearth

def birthdayCakeCandles(ar):
    lar = max(ar)
    count = 0
    for i in ar:
        if lar == i:
            count = count + 1
    
    return count

val = birthdayCakeCandles([44 ,53, 31 ,27 ,77 ,60 ,66 ,77 ,26 ,36])
print(val)
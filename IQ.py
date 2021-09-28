"""
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""

def iq_test(numbers):
    indexodd = 0
    indexeven = 0
    odd = 0
    even = 0
    numbers = numbers.split(" ")
    for i in range(0,len(numbers)):
        if int(numbers[i]) % 2 == 0:
            even += 1
            indexeven = i+1
        else:
            odd += 1
            indexodd = i+1
    
    if even == 1:
        return indexeven
    else:
        return indexodd
    
        

index = iq_test("2 4 7 8 10")
print(index)
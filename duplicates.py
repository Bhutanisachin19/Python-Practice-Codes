string = "hello sachin hello "
string = string.lower()
myset = set(string)
for i in myset:
    num = string.count(i)
    if num > 1:
        print("Number of times " + i + " appears is {}" .format(num))
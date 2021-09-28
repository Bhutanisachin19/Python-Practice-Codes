"""
Write a function that takes in a string of one or more words, and returns the same string
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

"""
def spin_words(sentence):
    s = " "
    mylist = sentence.split(" ")
    print(mylist)

    for i in range(0,len(mylist)):
        if len(mylist[i]) >= 5:
            mylist[i] = mylist[i][::-1]
    
    s = s.join(mylist)
    print(s)
    # Your code goes here
    #return

spin_words("hello kid wtf are you doing") 
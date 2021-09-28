# to check whether entered string pin is valid or not
# it should be of 4 or 6 digit and shoild contain only numbers
#return true or false

def validate_pin(pin):
    length = len(pin)
    if(length==4 or length==6):
        if(pin.isnumeric()):
            print("True")
        else:
            print("False")
    else:
        print("False")

validate_pin("+238")
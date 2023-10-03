#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # check if the character is lowercase
        if char >= 'a' and char <= 'z':
            # convert to uppercase by subtracting 32 from the ascii value
            upper = chr(ord(char) - 32)
        else:
            upper = char
        print(upper, end='')
    print()

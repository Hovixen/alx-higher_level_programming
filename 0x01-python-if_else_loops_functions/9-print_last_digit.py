#!/usr/bin/python3
def print_last_digit(number):
    # make the number absolute
    number = abs(number)
    # find the last digit
    lastDigit = number % 10

    print('{:d}'.format(lastDigit), end='')

    return lastDigit

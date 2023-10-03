#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = number % -10

if lastDigit > 5:
    digit = "and is greater than 5"
elif lastDigit == 0:
    digit = "and is 0"
else:
    digit = "and is less than 6 and not 0"

print(f'Last digit of {number} is {lastDigit} {digit}')

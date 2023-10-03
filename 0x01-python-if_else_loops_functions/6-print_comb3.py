#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0 and j == 1:
            print("{:02d}".format(1), end=", ")
        elif j == 9:
            print("{:02d}".format(i * 10 + j))
        else:
            print("{:02d}".format(i * 10 + j), end=", ")

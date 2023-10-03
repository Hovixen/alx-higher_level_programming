#!/usr/bin/python3
for i in range(90):
    if i % 10 > 1 / 10:
        if i != 89:
            print('{:02d}, '.format(i), end='')
        else:
            print('{:02d}'.format(i))

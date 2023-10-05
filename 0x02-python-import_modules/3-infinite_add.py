#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0

    for i in sys.argv[1:]:
        sums += int(i)
    print('{}'.format(sums))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_num = len(sys.argv) - 1

    if arg_num == 0:
        print('{:d} argument.'.format(arg_num))
    elif arg_num == 1:
        print('{:d} argument:'.format(arg_num))
        print('{:d}: {}'.format(arg_num, sys.argv[1]))
    else:
        print('{:d} arguments:'.format(arg_num))
        for i in range(1, arg_num + 1):
            print('{:d}: {}'.format(i, sys.argv[i]))

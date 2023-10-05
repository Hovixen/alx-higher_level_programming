#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: ./{} <a> operator <b>'.format(sys.argv[0]))
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    adds = add(a, b)
    subs = sub(a, b)
    muls = mul(a, b)
    divs = div(a, b)

    if sys.argv[2] == '+':
        print('{} {} {} = {}'.format(a, sys.argv[2], b, adds))
    elif sys.argv[2] == '-':
        print('{} {} {} = {}'.format(a, sys.argv[2], b, subs))
    elif sys.argv[2] == '*':
        print('{} {} {} = {}'.format(a, sys.argv[2], b, muls))
    elif sys.argv[2] == '/':
        print('{} {} {} = {}'.format(a, sys.argv[2], b, divs))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

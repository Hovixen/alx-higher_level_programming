#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    adds = add(a, b)
    subs = sub(a, b)
    muls = mul(a, b)
    divs = div(a, b)

    print('{:d} + {:d} = {:d}'.format(a, b, adds))
    print('{:d} - {:d} = {:d}'.format(a, b, subs))
    print('{:d} * {:d} = {:d}'.format(a, b, muls))
    print('{:d} / {:d} = {:d}'.format(a, b, divs))

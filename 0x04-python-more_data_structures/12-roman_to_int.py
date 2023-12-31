#!/usr/bin/python3
def roman_to_int(rom):
    if not isinstance(rom, str) or not rom:
        return 0
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sums = 0
    prev_num = 0
    for i in rom:
        if i in rom_dic:
            numeral = rom_dic[i]
            if numeral > prev_num:
                sums += numeral - 2 * prev_num
            else:
                sums += numeral
            prev_num = numeral
        else:
            # print("{} is not a Roman numeral".format(i))
            return 0
    return sums

#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # function divides element by element 2 in list
    ans = []

    try:
        for i in range(list_length):
            try:
                list_1 = float(my_list_1[i])
                list_2 = float(my_list_2[i])
                ans.append(list_1 / list_2)
            except (ValueError, TypeError):
                ans.append(0)
                print('wrong type')
            except ZeroDivisionError:
                ans.append(0)
                print('division by 0')
    except IndexError:
        print('out of range')
    finally:
        return ans

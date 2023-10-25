#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # function divides element by element 2 in list
    ans = []

    for i in range(list_length):
        try:
            list_1 = my_list_1[i]
            list_2 = my_list_2[i]
            result = (list_1 / list_2)
        except (ValueError, TypeError):
            result = 0
            print('wrong type')
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        except IndexError:
            result = 0
            print('out of range')
        finally:
            ans.append(result)
    return ans

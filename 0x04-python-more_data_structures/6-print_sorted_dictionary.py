#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # function prints a dictionary by ordered keys
    sorted_dic = sorted(a_dictionary)
    for keys in sorted_dic:
        # print('{}: {}'.format(keys, a_dictionary[keys]))
        print('{}:'.format(keys), '{}'.format(a_dictionary[keys]))

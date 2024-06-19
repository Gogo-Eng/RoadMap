#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
        for i in my_list[0:x]:
            print(i, end='')
        print()
        if x > len(my_list):
            return len(my_list)
        else:
            return x


my_list = [1,2,3,4]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
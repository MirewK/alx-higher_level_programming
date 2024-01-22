#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for i in range(x):
            element = my_list[i]
            try:
                print("{:d}".format(element), end="")
                printed_count += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        raise
    print()

    return printed_count

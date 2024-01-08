#!/usr/bin/python3
def print_list_integer(my_list = []):
    print(my_list, sep = "\n")
    print_list_integer(my_list)

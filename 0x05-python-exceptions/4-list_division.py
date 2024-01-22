#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        if len(my_list_1) < list_length or len(my_list_2) < list_length:
            raise ValueError("Out of range")

        for i in range(list_length):
            try:
                element1 = my_list_1[i]
                element2 = my_list_2[i]
                if isinstance(element1, (int, float)) and isinstance(element2, (int, float)):
                    result_list.append(element1 / element2)
                else:
                    print("wrong type")
                    result_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except IndexError:
                result_list.extend([0] * (list_length - len(result_list)))
        except ValueError as e:
            print(e)
            return None

        return result_list

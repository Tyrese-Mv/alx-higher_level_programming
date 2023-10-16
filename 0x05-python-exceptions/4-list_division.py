#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    try:
        for i in range(list_length):
            try:
                list1 = my_list_1[i] if i < len(my_list_1) else 0
                list2 = my_list_2[i] if i < len(my_list_2) else 1

                if not isinstance(list1, (int, float)) or not isinstance(list2, (int, float)):
                    raise ValueError("wrong type")
                if list2 == 0:
                    raise ZeroDivisionError("division by 0")
                res_list.append(list1 / list2)
            except ZeroDivisionError:
                print("division by 0")
                res_list.append(0)
            except ValueError as VE:
                print(VE)
                res_list.append(0)
            except IndexError:
                print("out of range")
                res_list.append(0)
    finally:
        return res_list

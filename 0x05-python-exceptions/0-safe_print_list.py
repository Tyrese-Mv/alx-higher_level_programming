#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count < x:
                print("{}".format(item), end="")
            else:
                break
    except:
        pass
    print()
    return count


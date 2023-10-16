#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)-32
        print("{}".format(chr(num)),end="")
    print()

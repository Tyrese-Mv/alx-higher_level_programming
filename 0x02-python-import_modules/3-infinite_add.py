#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    total = sum(int(arg) for arg in args)
    print(total)

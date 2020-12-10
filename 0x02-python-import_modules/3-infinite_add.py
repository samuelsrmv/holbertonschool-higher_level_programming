#!/usr/bin/python3
def add_num(long):
    add = 0
    for count in range(1, long):
        add = add + int(sys.argv[count])
    print(add)
if __name__ == "__main__":
    import sys
    long = len(sys.argv)
    add_num(long)
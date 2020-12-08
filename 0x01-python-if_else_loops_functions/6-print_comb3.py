#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j and i < j :
            if "{:d}{:d}".format(i, j) == "89": 
                print("{:d}{:d}".format(i, j), end="")
            else:
                print("{:d}{:d}, ".format(i, j), end="")
print("")

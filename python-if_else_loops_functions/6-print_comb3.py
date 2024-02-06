#!/usr/bin/python3
for i in range(0, 10):
    for b in range(i + 1, 10):
        if i == 8 and b == 9:
            print("{}{}".format(i, b))
        else:
            print("{}{}".format(i, b), end=", ")

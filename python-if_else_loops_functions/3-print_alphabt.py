#!/usr/bin/python3
import string
for i in string.ascii_lowercase:
    if i not in 'qe':
        print(i, end="")

#!/usr/bin/python3
from __future__ import print_function
#listRem = "\\x04\\x76\\x99\xf3".split("\\x")
listRem = "".split("\\x")
for x in range(1, 256):
    if "{:02x}".format(x) not in listRem:
        print("\\x" + "{:02x}".format(x), end='')
print()

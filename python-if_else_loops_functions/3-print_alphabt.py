#!/usr/bin/python3
for i in range(97, 123):
    if (not (i == 113 or i == 101)):
        print("{:c}".format(i), end="")

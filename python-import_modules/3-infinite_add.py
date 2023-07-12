#!/usr/bin/python3
def add_arg(argv):
    count = len(argv)
    suma = 0 
    for i in range(count - 1):
        suma = suma + int(argv[i + 1])
    print("{:d}".format(suma))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)

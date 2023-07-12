#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    suma = 0 
    for i in range(count - 1):
        suma = suma + int(sys.argv[i + 1])
    print("{:d}".format(suma))

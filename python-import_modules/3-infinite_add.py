#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    suma = 0
    if (count - 1 == 0):
        print("0")
    else: 
        for i in range(count - 1):
            suma = suma + int(sys.argv[i + 1])
        print("{}".format(suma))

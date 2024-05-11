#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    result = 0
    if len(argv) == 1:
        sys.exit("0")
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))

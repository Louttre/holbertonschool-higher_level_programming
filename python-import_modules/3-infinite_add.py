#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    result = 0
    if len(argv) == 1:
        sys.stderr.write("0\n")
        sys.exit(1)
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))

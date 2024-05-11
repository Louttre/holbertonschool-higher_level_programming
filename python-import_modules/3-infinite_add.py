#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    result = 0
    if len(argv) == 1:
        return result
    else:
        for i in range(1, len(argv) - 1):
            result += argv[i]
        return result

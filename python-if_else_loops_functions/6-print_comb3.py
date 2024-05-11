#!/usr/bin/python3
for i in range (0, 10):
    for j in range (0, 10):
        if j > i:
            print("{}".format(i), end='')
            if i < 8:
                print("{}".format(j), end=", ")
            else:
                print("{}".format(j), end='\n')
        else:
            continue

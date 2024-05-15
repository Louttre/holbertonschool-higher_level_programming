#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")
                a = float(my_list_1[i])
                b = float(my_list_2[i])
                if divisor == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(a / b)
            except ValueError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                result.append(0)
            except IndexError:
                result.append(0)
    finally:
        return result

#!/usr/bin/env python3

class VerboseList(list):

    def append(self, value):
        super().append(value)
        print("Added [{}] to the list.".format(value))
        

    def extend(self, value):
        super().extend(value)
        return "Extended the list with [{}] items.".format(value)

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)
        

    def pop(self, value):
        print("Popped [{}] from the list.".format(value))
        return super().pop(value)

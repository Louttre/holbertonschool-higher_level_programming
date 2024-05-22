#!/usr/bin/env python3
"""
This shebang line ensures the script runs with Python 3 interpreter.
"""


class VerboseList(list):
    """
    A custom list class that provides verbose notifications for list modifications.
    Inherits from the built-in list class.
    """

    def append(self, value):
        """
        Override the append method to provide a notification after adding an item to the list.
        """
        
        super().append(value)  # Call the append method of the base class (list)
        print("Added [{}] to the list.".format(value))

    def extend(self, value):
        """
        Override the extend method to provide a notification after extending the list with items from an iterable.
        """
        
        super().extend(value)
        print("Extended the list with [{}] items.".format(value))

    def remove(self, value):
        """
        Override the remove method to provide a notification after removing an item from the list.
        """
        
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)
        
    def pop(self, value=-1):
        """
        Override the pop method to provide a notification after removing and returning an item at a specific index.
        """
        
        print("Popped [{}] from the list.".format(self[value]))
        return super().pop(value)

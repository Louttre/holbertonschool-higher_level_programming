#!/usr/bin/env python3
"""
This shebang line ensures the script runs with Python 3 interpreter.
"""


class SwimMixin:
    def swim(self):
        """
        Print that the creature swims.
        """
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        """
        Print that the creature flies.
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """
        Print that the dragon roars.
        """
        print("The dragon roars!")

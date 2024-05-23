#!/usr/bin/env python3
"""
This shebang line ensures the script runs with Python 3 interpreter.
"""


class Fish:
    def swim(self):
        """
        Print that the fish is swimming.
        """
        print("The fish is swimming")
    
    def habitat(self):
        """
        Print the habitat of the fish.
        """
        print("The fish lives in water")

class Bird:
    def fly(self):
        """
        Print that the bird is flying.
        """
        print("The bird is flying")
    
    def habitat(self):
        """
        Print the habitat of the bird.
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        """
        Override the fly method to print that the flying fish is soaring.
        """
        print("The flying fish is soaring!")
    
    def swim(self):
        """
        Override the swim method to print that the flying fish is swimming.
        """
        print("The flying fish is swimming!")
    
    def habitat(self):
        """
        Override the habitat method to print that the flying fish lives both in water and the sky.
        """
        print("The flying fish lives both in water and the sky!")

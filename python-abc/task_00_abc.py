#!/usr/bin/env python3
"""
This shebang line ensures the script runs with the Python 3 interpreter.
"""

from abc import ABC, abstractmethod
"""
Importing ABC and abstractmethod from the abc module.
ABC is the base class for defining Abstract Base Classes (ABCs).
abstractmethod is a decorator indicating abstract 
methods that must be implemented by subclasses.
"""

class Animal(ABC):
    """
    Define an abstract base class named 'Animal' that inherits from ABC.
    Abstract base classes cannot be instantiated directly 
    and are used to define common interfaces for subclasses.
    """

    @abstractmethod
    def sound(self):
        """
        Define an abstract method 'sound' which must be implemented by any subclass of 'Animal'.
        Abstract methods do not contain any implementation in the base class.
        """
        pass

class Cat(Animal):
    """
    Define a class 'Cat' that inherits from the 'Animal' abstract base class.
    """
    
    def sound(self):
        """
        Implement the abstract method 'sound' for the 'Cat' class.
        """
        return "Meow"

class Dog(Animal):
    """
    Define a class 'Dog' that inherits from the 'Animal' abstract base class.
    """
    
    def sound(self):
        """
        Implement the abstract method 'sound' for the 'Dog' class.
        """
        return "Bark"

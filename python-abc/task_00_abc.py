#!/usr/bin/env python3
"""
abs module is imported for abstraction
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """The base class of all animals"""
    @abstractmethod
    def sound(self):
        """Abstract method for all derived classes"""
        pass


class Dog(Animal):
    """The dog is the subclass of animal"""
    def sound(self):
        """
        :return: A dog should bark
        """
        return "Bark"


class Cat(Animal):
    """The cat is the subclass of animal"""
    def sound(self):
        """
        :return: A cat should meow
        """
        return "Meow"

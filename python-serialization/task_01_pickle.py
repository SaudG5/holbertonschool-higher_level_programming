#!/usr/bin/env python3
"""Module that serializes and deserializes custom objects with pickle"""
import pickle


class CustomObject:
    """A simple object with a name, an age, and a student status"""

    def __init__(self, name, age, is_student):
        """Initialize the object with name, age, and is_student"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this object and save it to a file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an object from a pickle file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None

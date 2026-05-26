#!/usr/bin/python3
"""
Module for serializing and deserializing
a custom Python object using pickle.
"""

import pickle


class CustomObject:
    """
    Custom class with serialization methods.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): File where object will be saved.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): File to load the object from.

        Returns:
            CustomObject: The loaded object, or None if failed.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None

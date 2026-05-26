#!/usr/bin/python3
"""
Module for basic serialization and deserialization
using JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

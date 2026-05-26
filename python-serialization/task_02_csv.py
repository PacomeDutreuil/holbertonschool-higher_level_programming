#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV data to JSON format and save it to data.json.

    Args:
        filename (str): The CSV file to read.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Read CSV data
        with open(filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Write JSON data
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False

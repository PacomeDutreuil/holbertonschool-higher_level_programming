#!/usr/bin/python3
"""
Module for XML serialization and deserialization.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): XML output filename.
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create XML tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data into a Python dictionary.

    Args:
        filename (str): XML input filename.

    Returns:
        dict: Deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    # Rebuild dictionary from XML elements
    for child in root:
        data[child.tag] = child.text

    return data

#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str) -> None:
    """
    Serializes a Python dictionary into XML format.
    :param dictionary: The Python dictionary to serialize.
    :param filename: The name of the file to save the XML data.
    """
    try:
        # Create the root element
        root = ET.Element("data")
        # Iterate through the dictionary items
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        # Write the XML tree to the specified file
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Data successfully serialized to {filename}.")
    except Exception as e:
        print(f"An error occurred : {e}")


def deserialize_from_xml(filename: str) -> dict:
    """
    Deserializes XML data from a specified file into a Python dictionary.
    :param filename: The name of the file to read the XML data from.
    :return: A Python dictionary containing the deserialized XML data.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        # Initialize an empty dictionary to hold the deserialized data
        result = {}
        # Iterate through the XML elements and reconstruct the dictionary
        for child in root:
            result[child.tag] = child.text
        print(f"Data successfully deserialized from {filename}.")
        return result
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred while deserializing from XML: {e}")
        return {}

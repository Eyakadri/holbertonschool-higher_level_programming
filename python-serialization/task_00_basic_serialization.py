#!/usr/bin/env python3

import json
from typing import Dict, Optional


def serialize_and_save_to_file(data: Dict, filename: str) -> None:
    """
    Serializes a Python dictionary to a JSON file.

    :param data: Dictionary to serialize
    :param filename: Name of the file to save the JSON data
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
        print(f"Data successfully serialized and saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while serializing and saving to file: {e}")


def load_and_deserialize(filename: str) -> Optional[Dict]:
    """
    Loads a JSON file and deserializes it into a Python dictionary.

    :param filename: Name of the JSON file to read
    :return: Dictionary deserialized from the JSON file
    """
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        print(f"Data successfully loaded and deserialized from {filename}.")
        return data
    except Exception as e:
        print(f"An error occurred : {e}")
        return None

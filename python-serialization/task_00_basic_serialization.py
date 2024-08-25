#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.
    
    :param data: Dictionary to serialize
    :param filename: Name of the file to save the JSON data. If the file exists, it will be replaced.
    """
    try:
        with open(filename, 'w') as json_file:  # 'w' mode replaces the file if it already exists
            json.dump(data, json_file)
        print(f"Data serialized and saved to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred while serializing and saving to '{filename}': {e}")

def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it into a Python dictionary.
    
    :param filename: Name of the JSON file to read
    :return: Dictionary deserialized from JSON, or None if an error occurs
    """
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        print(f"Data loaded and deserialized from '{filename}' successfully.")
        return data
    except Exception as e:
        print(f"An error occurred while loading and deserializing from '{filename}': {e}")
        return None

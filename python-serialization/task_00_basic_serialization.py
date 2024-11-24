import json


def serialize_and_save_to_file(data, filename):
    """
Serialize a Python dictionary to JSON and save it to a file
    Args:
        data (dict): The dictionary to serialize
        filename (str): The output JSON file name
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error saving to file: {str(e)}")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file
    Args:
        filename (str): The input JSON file name
    Returns:
        dict: The deserialized dictionary
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading file: {str(e)}")
        return None

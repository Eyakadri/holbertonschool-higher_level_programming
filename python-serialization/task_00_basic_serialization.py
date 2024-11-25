import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.
    
    Args:
        data (dict): Dictionary to serialize
        filename (str): Output JSON filename
    """
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error serializing data: {e}")

def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.
    
    Args:
        filename (str): Input JSON filename
    
    Returns:
        dict: Deserialized dictionary from JSON file
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

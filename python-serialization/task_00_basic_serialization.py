import json

def serialize_and_save_to_file(data, filename):
   
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
    except Exception as e:
        print(f"An error occurred while serializing and saving to file: {e}")

def load_and_deserialize(filename):
    
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"An error occurred while loading and deserializing from file: {e}")
        return None

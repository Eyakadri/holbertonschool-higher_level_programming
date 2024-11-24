import json

def serialize_and_save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return None

def test_invalid_file_path():
    """
    Test handling of invalid file paths during serialization.
    """
    basic_data = {"test": "data"}
    invalid_path = "/invalid/path/test_data.json"
    
    try:
        serialize_and_save_to_file(basic_data, invalid_path)
        raise AssertionError("Expected OSError but no exception was raised")
    except OSError as e:
        print(f"Successfully caught expected error: {str(e)}")
        
    result = load_and_deserialize(invalid_path)
    assert result is None, "Expected None for invalid file path"
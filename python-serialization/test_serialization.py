#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

def test_serialization():
    # Test data
    test_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "hiking"],
        "contact": {
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
    }
    
    # Test serialization
    serialize_and_save_to_file(test_data, 'test_data.json')
    print("Data serialized and saved to 'test_data.json'")
    
    # Test deserialization
    loaded_data = load_and_deserialize('test_data.json')
    print("\nDeserialized data:")
    print(loaded_data)
    
    # Verify data integrity
    assert test_data == loaded_data, "Data integrity check failed!"
    print("\nData integrity check passed!")

if __name__ == "__main__":
    test_serialization()

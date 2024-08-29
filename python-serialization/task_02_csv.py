#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Converts data from a CSV file to JSON format and writes it to data.json.

    :param csv_filename: The name of the CSV file to convert.
    :return: True if the conversion was successful, False otherwise.
    """
    try:
        # Read the CSV file using DictReader
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]
        # Serialize the list of dictionaries to JSON
        with open('data.json', 'w') as json_file:
            json.dump(data_list, json_file, indent=4)
        print(f"Data from {csv_filename} has been converted to data.json.")
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

#!/usr/bin/env python3
"""
Module: csv, json.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to JSON format.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
        data = []
        for row in csv_reader:      
            data.append(row)
        json_data = json.dumps(data)
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)
        return True
    except (FileNotFoundError, Exception):
        return False

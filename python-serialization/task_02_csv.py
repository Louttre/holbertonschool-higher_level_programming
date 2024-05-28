#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(filename):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
        newdict = []
        for row in csv_reader:
            rows = [row]
            newdict.append(rows)
        json_csv = json.dumps(newdict)
        with open('json.data', 'w') as json_file:
            json_file.write(json_csv)
        return True
    except (FileNotFoundError, Exception):
        return False

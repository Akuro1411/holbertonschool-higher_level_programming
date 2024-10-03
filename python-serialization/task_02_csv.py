#!/usr/bin/env python3
"""
The csv and json modules are imported for serialization
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    :param file_name:
    :return: Converts the data to json format
    """
    try:
        with open(filename, mode="r", encoding="UTF-8") as file:
            data = csv.DictReader(file)
            data_list = []
            for i in data:
                data_list.append(i)
        with open("data.json", mode="w", encoding="UTF-8") as json_file:
            json.dump(data_list, fp=json_file)
        return True
    except FileNotFoundError:
        return False

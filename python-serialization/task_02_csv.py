#!/usr/bin/env python3
import csv, json


def convert_csv_to_json(filename):
    try:
        arr = []
        with open(filename, "r") as file:
            data = csv.DictReader(file)
            print(data)
            for i in data:
                # print(i)
                arr.append(i)
            print(arr)
            f = open("data.json", "w")
            json.dump(arr, f)
            f.close()
        return True
    except Exception as exc:
        print(f"We have an error like {exc}")
        return False

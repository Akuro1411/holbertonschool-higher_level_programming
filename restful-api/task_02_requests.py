#!/usr/bin/python3
"""
Modules for fetching data and writing them to the csv file
"""
import requests
import csv


def fetch_and_print_posts():
    """
    fetchs and prints data
    """
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = request.status_code
    print(f"Status Code: {status_code}")
    if status_code == 200:
        data = request.json()
        for i in data:
            print(i['title'])


def fetch_and_save_posts():
    """
    saves the posts to the csv file
    """
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = request.status_code
    file_name = "posts.csv"
    if status_code == 200:
        data = request.json()
        keys = ["id", "title", "body"]
        arr = []
        for i in data:
            dictionary = {}
            for j in keys:
                dictionary[j] = i[j]
            arr.append(dictionary)

        with open(file_name, 'w', encoding='UTF-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(arr)

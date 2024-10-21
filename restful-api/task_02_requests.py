#!/usr/bin/python3
"""
Modules for fetching data and writing them to the csv file
"""
import requests
import csv


def fetch_and_print_posts():
    """
    fetchs and prints posts
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    d = r.json()
    print(f"Status code: {r.status_code}")
    for i in d:
        print(i['title'])

def fetch_and_save_posts():
    """
    saves the posts to the file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    head_titles = ["id", "title", "body"]
    if r.status_code == 200:
        with open("posts.csv", "w", encoding="UTF-8") as file:
            writer = csv.DictWriter(file, fieldnames=head_titles)
            writer.writeheader()
            d = r.json()
            for i in d:
                row = {
                    "id": i["id"],
                    "title": i["title"],
                    "body": i["body"]
                }
                writer.writerow(row)

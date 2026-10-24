#!/usr/bin/python3
"""Fetches posts from JSONPlaceholder, prints titles and saves them to CSV."""
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts, print the status code and the title of each post."""
    response = requests.get(URL)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save their id, title and body to posts.csv."""
    response = requests.get(URL)
    if response.status_code == 200:
        posts = [{"id": post["id"], "title": post["title"],
                  "body": post["body"]} for post in response.json()]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)

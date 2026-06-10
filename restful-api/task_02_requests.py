#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts and print their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts and save them to posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(data)

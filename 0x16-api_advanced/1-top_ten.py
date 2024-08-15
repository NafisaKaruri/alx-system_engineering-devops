#!/usr/bin/python3
"""
Function that queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    prints the titles of the first 10 hot posts listed
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if r.status_code == 200:
        for child in r.json().get("data").get("children"):
            title = child.get("data").get("title")
            print(title)
    else:
        print(None)

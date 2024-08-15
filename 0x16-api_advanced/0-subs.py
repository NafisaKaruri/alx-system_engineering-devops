#!/usr/bin/python3
"""
Function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    Returns: the number of subscribers for a given subreddit
             0 if not a valid subreddit
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"},
    )

    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0

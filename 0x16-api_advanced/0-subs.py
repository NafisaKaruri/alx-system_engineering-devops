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
        headers={"User-Agent": "Custom"},
    )

    if r.status_code == 200:
        return r.json().get("data", {}).get("subscribers", 0)
    else:
        return 0

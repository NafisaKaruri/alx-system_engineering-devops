#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API
    Returns: list of titles of all hot articles
             if none found returns None
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if r.status_code == 200:
        for child in r.json().get("data").get("children"):
            d = child.get("data")
            title = d.get("title")
            hot_list.append(title)
        
        after = r.json().get("data").get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None


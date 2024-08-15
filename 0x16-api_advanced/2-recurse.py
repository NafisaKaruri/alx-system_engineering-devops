#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list[]):
    """
    Recursive function that queries the Reddit API
    Returns: list of titles of all hot articles
             if non found returns None
    """
    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after, "count": count, "limit": 100},
    )

    if r.status_code == 200:
        d = r.json().get("data")
        after = d.get("after"):
        count += d.get("dist")
        for child in d.get("children"):
            hot_list.append(child.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list)
        return hot_list
    else:
        return None

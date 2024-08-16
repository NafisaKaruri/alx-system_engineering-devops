#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, count=None, after=None):
    """
    Recursive function that queries the Reddit API
    parses the title of all hot articles, then
    prints a sorted count of given keywords
    """
    if count is None:
        count = defaultdict(int)

    r = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if r.status_code == 200:
        data = r.json().get('data', {})
        children = data.get('children', [])

        if not children:
            sorted_count = sorted(count.items(),
                                  key=lambda x: (-x[1], x[0]))
            for word, cnt in sorted_count:
                print("{}: {}".format(word, cnt))
            return

        for child in children:
            title = child['data'].get('title', '').lower()
            for word in word_list:
                prn = r'\b{}\b'.format(re.escape(word.lower()))
                matches = re.findall(prn, title, re.IGNORECASE)
                count[word.lower()] += len(matches)

        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, count,
                               after)
        return None

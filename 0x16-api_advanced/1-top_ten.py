#!/usr/bin/python3
"""Module to display hot posts
"""

import requests


def top_ten(subreddit):
    """Method that displays the titles of the 10 hottest post on a given
       subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/10.0"}

    params = {"limit": 10}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")

    [print(c.get("data").get("title")) for c in results.get("children")]

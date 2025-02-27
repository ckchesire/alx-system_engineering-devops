#!/usr/bin/python3
"""Module to query subscribers on a Reddit subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Method returns the total number of subscribers on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/10.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

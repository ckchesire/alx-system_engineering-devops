#!/usr/bin/python3
"""Module to query a list of all hot posts on a particular Reddit Subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Method recursively retrieves a list of titles of all posts on a given
       subreddit.
    """
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    headers = {"User-Agent" : "Mozilla/10.0"}

    params = {
            "after" : after
            "count" : count
            "limit" : 1000
            }
    response = request.get(url, headers=headers, params=params, 
            allow_redirect=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list

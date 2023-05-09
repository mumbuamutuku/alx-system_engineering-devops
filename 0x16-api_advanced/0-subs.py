#!/usr/bin/python3
"""  returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """return no. of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    res = r.json().get("data")
    return res.get("subscribers")

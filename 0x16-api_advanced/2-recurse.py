#!/usr/bin/python3
""" function that queries the Reddit API
    returns a list containing the titles of all hot articles."""
import requests


def recurse(subreddit, hot_list=[], after="", c=0):
    """prints list of the titles of the all hot articles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    p = {
            "after": after,
            "c": c,
            "limit": 100
            }
    resp = requests.get(url, headers=h, params=p, allow_redirects=False)
    if resp.status_code == 404:
        return None

    res = resp.json().get("data")
    after = res.get("after")
    c += res.get("dist")
    for j in res.get("children"):
        hot_list.append(j.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, c)
    return hot_list

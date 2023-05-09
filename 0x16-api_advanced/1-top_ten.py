#!/usr/bin/python3
""" function that queries the Reddit API
    prints the titles of the first 10 hot posts listed."""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    p = {
            "limit": 10
            }
    resp = requests.get(url, h=h, p=p, allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    res = resp.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]

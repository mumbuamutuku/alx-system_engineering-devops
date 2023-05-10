#!/usr/bin/python3
""" function that queries the Reddit API
    returns a list containing the titles of all hot articles."""
import requests


def count_words(subreddit, word_list, instances={}, after="", c=0):
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
    try:
        res = resp.json()
        if resp.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    res = resp.json().get("data")
    after = res.get("after")
    c += res.get("dist")
    for j in res.get("children"):
        title = j.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, c)

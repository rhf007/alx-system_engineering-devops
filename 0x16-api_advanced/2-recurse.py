#!/usr/bin/python3
"""recurse"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """recurse"""
    user_ag = {'User-Agent': 'BW_121'}
    sho = {'show': 'all'}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?after={}".
                       format(subreddit, after), headers=user_ag, params=sho)

    if res:
        data = res.json().get("data").get("children")
        data2 = res.json().get("data").get("after")
        if after is None:
            return hot_list
        for d in data:
            hot_list.append(d.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    else:
        print("None")

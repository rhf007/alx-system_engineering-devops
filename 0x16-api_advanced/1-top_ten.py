#!/usr/bin/python3
"""top 10"""


import requests


def number_of_subscribers(subreddit):
    """getting sub info"""
    user_ag = {'User-Agent': 'BW_121'}
    lim = {'limit': 10}
    res = requests.get("https://www.reddit.com/r/{}/hot.json".
                            format(subreddit), headers=user_ag, params=lim)

    if res:
        data = res.json().get("data").get("children")
        for d in data:
            print(d.get('data').get('title'))
    else:
        print("None")

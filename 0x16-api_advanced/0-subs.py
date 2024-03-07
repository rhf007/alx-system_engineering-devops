#!/usr/bin/python3
"""subs"""

import requests


def number_of_subscribers(subreddit):
    """getting sub info"""
    user_ag = {'User-Agent': 'BW_121'}
    res = requests.get("https://www.reddit.com/r/{}/about.json".
                       format(subreddit), headers=user_ag)

    if res:
        return(res.json().get("data").get("subscribers"))
    else:
        return(0)

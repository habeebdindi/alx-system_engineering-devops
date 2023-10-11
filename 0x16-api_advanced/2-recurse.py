#!/usr/bin/python3
"""Module contains a recursive function
"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """recursive function that queries the Reddit API and returns a list
       containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    user = {"User-Agent": "habeebdindi"}
    response = requests.get(url, params=params, headers=user,
                            allow_redirects=False)
    if response.status_code == requests.codes.OK:
        data = response.json()
        children = data.get('data', {}).get('children', [])
        for child in children:
            hot_list.append(child['data']['title'])
        after = data.get('data', {}).get('after')
        if after:
            params['after'] = after
            recurse(subreddit, hot_list, params)

    return hot_list

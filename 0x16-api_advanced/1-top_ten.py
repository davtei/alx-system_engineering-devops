#!/usr/bin/python3
"""A Python script that queries the Reddit API using request module."""
import requests


def top_ten(subreddit):
    """A function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("title")) for c in results.get("children")]

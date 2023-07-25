#!/usr/bin/python3
"""A Python script that returns information about a given employee ID's
TODO list progress."""

import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todo", params={"userId": user_id}).json()

    completed = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(c)) for c in completed]

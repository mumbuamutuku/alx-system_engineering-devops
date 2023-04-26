#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.jsom".format(user_id), "w") as jsnfile:
        json.dump{user_id: [{
            "task": t.get("title")
            "completed": t.get("completed"),
            "username": username
            } for t in todos]}, jsnfile)

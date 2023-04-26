#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
import sys

if __name__ =="__main__":
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "u/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todo", params={"userId": sys.argv[1]}).json()

    done = [j.get("title") for j in todo if j.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(u.get("name"), len(done), len(todo)))
    [print("\t{}".format(c)) for c in done]

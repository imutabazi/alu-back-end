#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details to get the username
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the TODO list for this specific user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Format list of dictionaries according to specifications
    task_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    # Write data to USER_ID.json
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: task_list}, jsonfile)

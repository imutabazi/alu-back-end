#!/usr/bin/python3
"""Returns information about a given employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    employee_name = user.get("name")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    completed_tasks = [
        task.get("title") for task in todos if task.get("completed") is True
    ]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)))

    for task_title in completed_tasks:
        print("\t {}".format(task_title))

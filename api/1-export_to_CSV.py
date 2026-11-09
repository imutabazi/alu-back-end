#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
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

    # Write the data to a CSV file named after the user ID
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"),
                             task.get("title")])

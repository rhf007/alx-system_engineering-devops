#!/usr/bin/python3
"""Gather data from an API"""


import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    idd = int(argv[1])
    users = get('https://jsonplaceholder.typicode.com/users').json()
    todos = get('https://jsonplaceholder.typicode.com/todos').json()
    # print(users)
    # print(type(users))
    user_tasks = []
    completed_tasks = 0
    total_tasks = 0
    emp_username = ""
    task_stat = ""
    task_title = ""
    rows = []

    for user in users:
        if user.get("id") == idd:
            emp_username = user.get("username")

    for todo in todos:
        if todo.get("userId") == idd:
            task_stat = todo.get("completed")
            task_title = todo.get("title")
            rows.append([idd, emp_username, task_stat, task_title])

    with open(f"{idd}.csv", "w", newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerows(rows)

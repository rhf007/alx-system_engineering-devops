#!/usr/bin/python3
"""Gather data from an API"""


import json
from requests import get
from sys import argv


if __name__ == "__main__":
    idd = int(argv[1])
    users = get('https://jsonplaceholder.typicode.com/users').json()
    todos = get('https://jsonplaceholder.typicode.com/todos').json()
    # print(users)
    # print(type(users))
    user_tasks = {str(idd): []}
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
            user_tasks[str(idd)].append({
                                "task": task_title,
                                "completed": task_stat,
                                "username": emp_username
            })

    json_user_tasks = json.dumps(user_tasks)

    with open(f"{idd}.json", "w", newline='') as f:
        f.write(json_user_tasks)

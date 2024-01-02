#!/usr/bin/python3
"""Gather data from an API"""

import json
from requests import get

if __name__ == "__main__":
    users = get('https://jsonplaceholder.typicode.com/users').json()
    todos = get('https://jsonplaceholder.typicode.com/todos').json()

    all_user_tasks = {}

    for user in users:
        user_id = str(user["id"])
        emp_username = user["username"]
        user_tasks = []

        for todo in todos:
            if todo.get("userId") == user["id"]:
                task_stat = todo.get("completed")
                task_title = todo.get("title")

                user_tasks.append({
                    "username": emp_username,
                    "task": task_title,
                    "completed": task_stat
                })

        all_user_tasks[user_id] = user_tasks

    json_data = json.dumps(all_user_tasks)

    with open("todo_all_employees.json", "w") as f:
        f.write(json_data)

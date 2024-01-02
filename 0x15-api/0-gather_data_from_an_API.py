#!/usr/bin/python3
"""Gather data from an API"""


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
    emp_name = ""

    for user in users:
        if user.get("id") == idd:
            emp_name = user.get("name")

    for todo in todos:
        if todo.get("userId") == idd:
            total_tasks += 1
            if todo.get("completed"):
                completed_tasks += 1
                user_tasks.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(emp_name,
                                                          completed_tasks,
                                                          total_tasks))

    for task in user_tasks:
        print("\t {}".format(task))

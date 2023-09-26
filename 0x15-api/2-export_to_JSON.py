#!/usr/bin/python3
"""Records all tasks that are owned by this employee in json file
"""
import requests
import sys


if __name__ == "__main__":
    json_f = '{}.json'.format(sys.argv[1])
    name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        sys.argv[1])
    name = requests.get(name_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    todo = requests.get(todo_url).json()

    with open(json_f, 'w', newline='') as f:
        tasks = [dict(task=t['title'], completed=t['completed'],
                 username=name['username']) for t in todo]
        ret_dict = {}
        ret_dict[argv[1]] = tasks
        json.dumps(ret_dict, f)

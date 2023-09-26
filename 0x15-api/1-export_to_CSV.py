#!/usr/bin/python3
"""Records all tasks that are owned by this employee
"""
import requests
import sys


if __name__ == "__main__":
    csv_f = '{}.csv'.format(sys.argv[1])
    name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        sys.argv[1])
    name = requests.get(name_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    todo = requests.get(todo_url).json()

    with open(csv_f, 'w', newline='') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todo:
            write.writerow([name['id'], name['username'],
                            t['completed'], t['title']])

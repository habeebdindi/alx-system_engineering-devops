#!/usr/bin/python3
""" Given employee ID, returns information about TODO list progress """


if __name__ == '__main__':

    import requests
    import json

    ret_dict = {}
    for user_id in range(1, 11):
        name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            user_id)
        name = requests.get(name_url).json()
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={} \
                   ".format(user_id)
        todo = requests.get(todo_url).json()

        ret_dict[user_id] = [dict(task=t['title'],
                                  completed=t['completed'],
                                  username=name['username']) for t in todo]

    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(ret_dict))

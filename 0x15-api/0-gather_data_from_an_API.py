#!/usr/bin/python3
'''
gather employee data from API
'''

import re
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/"
userID = sys.argv[1]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            res_name = requests.get(BASE_URL + f"users/{userID}")
            name = res_name.json().get("name")
            todos = requests.get(BASE_URL + f"todos?userId={userID}").json()
            completed = [todo for todo in todos
                         if todo.get("completed")
                         is True]

            print("Employee {} is done with tasks {}/{}:"
                  .format(name, len(completed), len(todos)))

            if len(todos) > 1:
                for todo in todos:
                    print("\t{}".format(todo.get("title")))
        except Exception as e:
            print(e)

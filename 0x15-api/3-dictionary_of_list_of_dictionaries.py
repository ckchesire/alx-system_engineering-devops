#!/usr/bin/python3
"""Module to fetch and export all employees TODO lists
"""
import json
import requests


def get_users_dict():
    """Method to retrieve all the employees TODO lists

       Return:
          returns a dictionary of the employees TODO lists
    """
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(f"{url}users").json()

    data_dict = {}

    for user in users:
        employee_id = user["id"]

        todo_response = requests.get(f"{url}todos?userId={employee_id}")
        todo_list = todo_response.json()

        data_dict[employee_id] = []

        for todo in todo_list:
            task_info = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
                    }
            data_dict[employee_id].append(task_info)

    return data_dict


if __name__ == "__main__":
    data_export = get_users_dict()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)

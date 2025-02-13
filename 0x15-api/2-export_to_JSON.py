#!/usr/bin/python3
"""Module to record all tasks that are owned by an employee
"""
import json
import requests
import sys


def json_export_tasklist(employee_id):
    """Method gets record of tasks owned by an employee

      Args:
        employee_id - particular id of the employee record

      Return:
         returns csv file of tasks owned by an employee
    """
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f"{url}users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: Invalid employee ID")
        return

    user = user_response.json()
    user_name = user.get("username")

    params = {"userId": employee_id}

    todos_response = requests.get(f"{url}todos", params=params)
    tasks = todos_response.json()

    data_export = {employee_id: []}

    for task in tasks:
        task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
                }
        data_export[employee_id].append(task_info)

    filename = f"{employee_id}.json"

    with open(filename, "w") as jsonfile:
        json.dump(data_export, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("./1-export_to_CSV.py <employee_id>")
    else:
        json_export_tasklist(sys.argv[1])

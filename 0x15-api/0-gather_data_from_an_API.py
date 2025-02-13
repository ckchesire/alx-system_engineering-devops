#!/usr/bin/python3
import requests
import sys
"""Module to display the TODO list progress of and employee
"""


def get_todo_progress(employee_id):
    """Method to display the employee TODO list progress

       Args:
           employee_id - integer parameter which is the employeed ID

       Returns:
           Returns formatted employee TODO list progress
    """
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f"{url}users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: Invalid Employee ID.")
        return

    user = user_response.json()
    employee_name = user.get("name")

    params = {"userId": employee_id}
    todos_response = requests.get(f"{url}todos", params=params)

    todos = todos_response.json()

    completed_tasks = [todo for todo in todos if todo.get("completed")]
    total_tasks = len(todos)
    total_done = len(completed_tasks)

    print("Employee {} is done with tasks ({}/{})".format(employee_name,
                                                          total_done,
                                                          total_tasks))
    for completed in completed_tasks:
        print(f"\t {completed.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        get_todo_progress(sys.argv[1])

#!/usr/bin/python3
"""Module to record all tasks that are owned by an employee
"""
import sys
import csv
import requests


def get_csv_tasklist(employee_id):
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

    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id,
                             user_name,
                             task.get("completed"),
                             task.get("title")]
                            )


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("./1-export_to_CSV.py <employee_id>")
    else:
        get_csv_tasklist(sys.argv[1])

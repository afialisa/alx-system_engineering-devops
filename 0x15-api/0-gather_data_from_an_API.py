#!/usr/bin/python3
"""
A python script that collects and displays an employee's TODO list progress.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Collects and displays the TODO list progress of a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        return

    # Collect employee data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if not employee_data:
        print("Employee not found.")
        return

    employee_name = employee_data.get('name')

    # Collect TODO list data
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee_todo_progress(sys.argv[1])

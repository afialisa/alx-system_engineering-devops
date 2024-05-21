#!/usr/bin/python3
"""
A python script that exports an employee's TODO list progress in CSV format.
"""

import csv
import requests
import sys


def export_employee_todo_to_csv(employee_id):
    """
    Exports the TODO list progress of a given employee in CSV format.

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
    employee_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if not employee_data:
        print("Employee not found.")
        return

    employee_name = employee_data.get('name')

    # Collect TODO list data
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare CSV file name
    csv_filename = f"{employee_id}.csv"

    # Write TODO list progress to CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = (
                ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        )
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task.get('completed')),
                'TASK_TITLE': task.get('title')
            })

    print(f"TODO list exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        export_employee_todo_to_csv(sys.argv[1])

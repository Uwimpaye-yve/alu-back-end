#!/usr/bin/python3
"""
Script to fetch and display an employee's TODO list progress using a REST API.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch employee details for ID {employee_id}.")
        return
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}.")
        return
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]

    # Display progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
for task in completed_tasks:
        print(f"\t {task.get('title')}")

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

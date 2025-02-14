#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetches and displays the TODO list progress for an employee."""
    
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print("Error: Invalid employee ID or API not reachable")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name', 'Unknown')
    completed_tasks = [task['title'] for task in todos_data if task.get('completed')]

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos_data)}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer")
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

#!/usr/bin/python3
import requests
import sys
def get_employee_todo_progress(employee_id):
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos").json()
    employee_name = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()['name']
    completed_tasks = [task['title'] for task in todos if task['completed']]
    
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            get_employee_todo_progress(int(sys.argv[1]))
        except ValueError:
            print("Employee ID must be an integer")
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")

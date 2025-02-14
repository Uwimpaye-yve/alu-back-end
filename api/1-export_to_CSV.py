#!/usr/bin/python3
import csv
import requests
import sys

def export_employee_todo_to_csv(employee_id):
    """
    Fetches the TODO list for an employee and exports it to a CSV file.
    
    Args:
    employee_id (int): The ID of the employee.
    
    Returns:
    None: Saves the employee's task data to a CSV file.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()
    
    employee_username = user.get("username")
    
    file_name = f"{employee_id}.csv"
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_username, task["completed"], task["title"]])
    
    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    """
    Main function to handle command-line input and trigger the CSV export.
    """
    if len(sys.argv) == 2:
        try:
            export_employee_todo_to_csv(int(sys.argv[1]))
        except ValueError:
            print("Employee ID must be an integer")
    else:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")

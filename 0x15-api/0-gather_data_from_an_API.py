#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress.
"""

import requests
import sys

# Check that an employee ID has been provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

# Retrieve the employee's TODO list
employee_id = sys.argv[1]
response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(employee_id))
todos = response.json()

# Count the number of completed tasks and the total number of tasks
num_completed_tasks = sum(1 for todo in todos if todo['completed'])
total_num_tasks = len(todos)

# Print the employee TODO list progress in the required format
employee_name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(employee_id)).json()['name']
print("Employee {} is done with tasks({}/{}):"
      .format(employee_name, num_completed_tasks, total_num_tasks))
for todo in todos:
    if todo['completed']:
        print("\t {} {}".format('\t', todo['title']))

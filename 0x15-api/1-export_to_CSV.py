#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress.
"""

import csv
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
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
response_user = requests.get(url_user)
user = response_user.json()

# Export tasks to CSV file
csv_filename = "{}.csv".format(employee_id)

with open(csv_filename, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",",
                        quotechar='"', quoting=csv.QUOTE_ALL)

    for todo in todos:
        writer.writerow([todo.get("userId"), user['username'],
                        todo.get("completed"), todo.get("title")])

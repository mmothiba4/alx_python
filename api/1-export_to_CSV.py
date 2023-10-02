#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/1".format(USER_ID))
    USERNAME = user.json.get("USERNAME")
    todos = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")

filename = USER_ID.csv
with open(filename, mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
    for task in todos.json():
        if task.get('USER_ID') == int(USER_ID):
            writer.writerow([USER_ID, name, str(task.get('TASK_COMPLETED_STATUS')),task.get('TASK_TITLE')])
#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/1".format(userId))
    username = user.json.get("username")
    todos = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")

filename = userId + '.csv'
with open(filename, mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
    for task in todos.json():
        if task.get('userId') == int(userId):
            writer.writerow([userId, name, str(task.get('completed')),task.get('title')])

if __name__ == "__main__":
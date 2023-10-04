"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress and counts tasks in the CSV.
"""

import re
import requests
import sys
import csv

API_URL = 'https://jsonplaceholder.typicode.com'

def user_info(id):
    user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
    todos_res = requests.get('{}/todos'.format(API_URL)).json()
    user_name = user_res.get('username')
    todos = list(filter(lambda x: x.get('userId') == id, todos_res))

    csv_filename = '{}.csv'.format(id)

    try:
        with open(csv_filename, 'r') as f:
            csv_data = list(csv.reader(f))
            num_tasks = len(csv_data) - 1  # Subtract 1 to exclude the header row
            print(f'Number of tasks in CSV: {num_tasks} OK')
    except FileNotFoundError:
        print(f'CSV file {csv_filename} not found.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_info(id)
    else:
        print("Please provide a valid user ID as a command-line argument.")

#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/1"
    user = requests.get(url.format(user_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []
    
    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'), "completed": task.get('completed'), "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
#!/usr/bin/python3
"""This script fetches data from
    https://alu-intranet.hbtn.io/status
"""


import requests

def fetch_r():
    """ fetches https://alu-intranet.hbtn.io/status """
    req = requests.get('https://alu-intranet.hbtn.io/status')
    s = "Body response:\n\t- type: {}\n\t- content: {}"
    print(s.format(type(req.text), req.text))


if __name__ == "__main__":
    fetch_r()
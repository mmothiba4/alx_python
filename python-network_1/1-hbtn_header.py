#!/usr/bin/python3
"""A script that takes in a URL,
Sends a request to the URL,
And displays the value of the X-Request-Id
variable found in the header ofthe response.
"""

import sys
import requests


def request_id():
    """ displays the value of the X-Request-Id variable """
    with urllib.request.urlopen(argv[1]) as response:
        the_page = response.info()
    print(the_page['X-Request-Id'])


if __name__ == "__main__":
    request_id()
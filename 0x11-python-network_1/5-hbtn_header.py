#!/usr/bin/python3
"""
Script takes a Url
Sends request to Url and displays value
of the X-Request-id variable found in the header of response
"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    head = "X-Request-Id"

    response = requests.get(url)

    if response.status_code == 200:
        Id = response.headers.get(head)
        print('{}'.format(Id))

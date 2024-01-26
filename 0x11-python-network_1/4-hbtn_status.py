#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    if response.status_code == 200:
        body = response.text
        print("Body response:")
        print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

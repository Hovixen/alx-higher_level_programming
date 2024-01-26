#!/usr/bin/python3
"""
Script takes a Url, sends request and displays the body
of the response (decoded in uft-8)
"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        body = response.text
        print('{}'.format(body))

    else:
        print("Error code: {}".format(response.status_code))

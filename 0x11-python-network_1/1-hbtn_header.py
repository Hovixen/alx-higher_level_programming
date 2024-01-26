#!/usr/bin/python3
"""
Script takes a Url
Sends request to Url and displays value
of the X-Request-id variable found in the header of response
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as res:
        Id = res.headers.get('X-Request-Id')
        print('{}'.format(Id))

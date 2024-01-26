#!/usr/bin/python3
"""
Script takes a Url, sends request and displays the body
of the response (decoded in uft-8)
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            content = res.read().decode('utf-8')
            print('{}'.format(content))

    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

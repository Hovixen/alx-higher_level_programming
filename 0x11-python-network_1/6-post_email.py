#!/usr/bin/python3
"""
Script takes Url and email, sends a POST request
to the passed Url with the email as parameter and displays body
of the response (decoded in utf8)
"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    response = requests.post(url, data=data)

    if response.status_code == 200:
        res = response.text

        print('{}'.format(res))

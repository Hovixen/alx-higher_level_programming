#!/usr/bin/python3
"""
Script takes Url and email, sends a POST request
to the passed Url with the email as parameter and displays body
of the response (decoded in utf8)
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    encode_data = urllib.parse.urlencode(data).encode('utf-8')

    with urllib.request.urlopen(url, data=encode_data) as res:
        content = res.read().decode('utf-8')

        print(content)

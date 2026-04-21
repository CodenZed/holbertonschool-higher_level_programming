#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # The email must be sent in the 'email' variable
    values = {'email': email}

    # Encode the data to be used in the POST request
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Data should be bytes

    req = urllib.request.Request(url, data)

    # Use the 'with' statement for the request
    with urllib.request.urlopen(req) as response:
        # Decode and display the body of the response in utf-8
        print(response.read().decode('utf-8'))

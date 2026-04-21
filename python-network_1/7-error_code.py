#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the status code is >= 400, prints the error code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    # Send the GET request
    r = requests.get(url)

    # Check if the status code indicates an error (>= 400)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        # Display the body of the response
        print(r.text)

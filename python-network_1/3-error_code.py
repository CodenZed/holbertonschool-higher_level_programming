#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTP errors by printing the error code.
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Use the 'with' statement for the request
        with urllib.request.urlopen(url) as response:
            # Decode and display the body in utf-8
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Manage HTTPError exceptions and print the status code
        print("Error code: {}".format(e.code))

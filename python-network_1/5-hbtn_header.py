#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the 
X-Request-Id variable found in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    # Send the GET request
    r = requests.get(url)
    
    # Access the headers dictionary and get the specific key
    # .get() is safer as it won't crash if the header is missing
    print(r.headers.get('X-Request-Id'))

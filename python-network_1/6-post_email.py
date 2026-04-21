#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the response body.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Payload dictionary containing the email variable
    payload = {'email': email}

    # Send the POST request
    r = requests.post(url, data=payload)

    # Display the body of the response
    print(r.text)

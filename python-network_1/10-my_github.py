#!/usr/bin/python3
"""
Uses GitHub API to display the user id using Basic Authentication.
The script takes a username and a personal access token as arguments.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    # Use Basic Authentication with username and PAT
    r = requests.get(url, auth=(username, token))

    try:
        # Parse response as JSON
        user_data = r.json()

        # Display the 'id' value if found, otherwise None
        # GitHub returns a JSON with an 'id' key on success
        # If authentication fails, 'id' won't be in the response
        print(user_data.get('id'))
    except ValueError:
        # Handle cases where the response is not valid JSON
        print("None")

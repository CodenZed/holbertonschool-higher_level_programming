#!/usr/bin/python3
"""
Uses GitHub API to display the user id using Basic Authentication.
Arguments: username, personal access token.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token = sys.argv[2]
        url = "https://api.github.com/user"

        # auth=(user, pass) sends the Basic Auth header automatically
        r = requests.get(url, auth=(username, token))
        
        try:
            json_dict = r.json()
            print(json_dict.get('id'))
        except ValueError:
            print("None")

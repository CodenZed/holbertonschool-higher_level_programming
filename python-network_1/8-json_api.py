#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # Get letter from arguments or default to empty string
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        # Send POST request
        r = requests.post(url, data=payload)
        
        # Parse JSON response
        response_json = r.json()

        if not response_json:
            print("No result")
        else:
            # Safely get id and name
            u_id = response_json.get('id')
            u_name = response_json.get('name')
            print("[{}] {}".format(u_id, u_name))

    except ValueError:
        # Handle invalid JSON formatting
        print("Not a valid JSON")

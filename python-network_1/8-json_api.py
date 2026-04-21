#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
Handles JSON validation and empty results.
"""
import requests
import sys


if __name__ == "__main__":
    # Determine the search letter 'q'
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        # Send the POST request
        r = requests.post(url, data=payload)

        # Parse the response as JSON
        # requests.json() raises a ValueError if the response is not valid JSON
        response_json = r.json()

        if not response_json:
            print("No result")
        else:
            # Display the id and name if the dictionary is not empty
            user_id = response_json.get('id')
            user_name = response_json.get('name')
            print("[{}] {}".format(user_id, user_name))

    except ValueError:
        # Catch JSON decoding errors
        print("Not a valid JSON")

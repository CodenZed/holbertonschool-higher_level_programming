#!/usr/bin/python3
"""
Lists 10 commits (from most recent to oldest) of a repository.
Usage: ./100-github_commits.py <repository name> <owner name>
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    
    try:
        # The API returns a list of commit dictionaries
        commits = r.json()
        
        # Iterate through the first 10 commits
        for commit in commits[:10]:
            sha = commit.get('sha')
            # The author name is nested: commit -> author -> name
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
            
    except (ValueError, IndexError, AttributeError):
        # Handle cases where the response isn't what we expect
        pass

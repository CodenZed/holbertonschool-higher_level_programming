#!/bin/bash
# Takes a URL and prints the size of the response body in bytes
curl -s "$1" | wc -c

# header_checker.py
# Checks HTTP security headers on a given URL
# Usage: python header_checker.py <url>

import sys #Access to command-line arguments 
import requests #HTTP requests

if len(sys.argv) < 2: # sys.argv is a list of command-line arguments
    print("Usage: python header_checker.py <url>")
    sys.exit(1) # Exit the program with an error code

url = sys.argv[1] # The URL to check

try:
    response = requests.get(url) # Send a GET request to the URL, store the response in the response variable
    response.raise_for_status() # Raise an exception for bad status codes
except requests.exceptions.RequestException as e: # If an exception occurs, print the error and exit the program
    print(f"Error: {e}")
    sys.exit(1) # Exit the program

print(f"Headers for {url}:")

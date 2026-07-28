# header_checker.py
# Checks HTTP security headers on a given URL
# Usage: python header_checker.py <url>

import sys #Access to command-line arguments 
import requests #HTTP requests

if len(sys.argv) < 2: # sys.argv is a list of command-line arguments
    print("Usage: python header_checker.py <url>")
    sys.exit(1) # Exit the program with an error code

url = sys.argv[1] # The URL to check

HEADERS_TO_CHECK = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
] # List of headers to check
# strict-transport-security: Forces HTTPS, prevents downgrade attacks
# content-security-policy: Prevents XSS by restricting what scripts can load
# x-frame-options: Prevents clickjacking (site loaded in iframe)
# x-content-type-options: Prevents MIME sniffing attacks
# referrer-policy: Controls what URL info is sent to other sites

try:
    response = requests.get(url) # Send a GET request to the URL, store the response in the response variable
    response.raise_for_status() # Raise an exception for bad status codes
except requests.exceptions.RequestException as e: # If an exception occurs, print the error and exit the program
    print(f"Error: {e}")
    sys.exit(1) # Exit the program
print(f"\nChecking: {url}")
print("=" * 50) # Print a separator line

passed = 0 # Count the number of headers that are present

for header in HEADERS_TO_CHECK: # Iterate over the headers-list to check
    if header in response.headers: # response.headers is a dictionary of the headers sent by server, true or false
        print(f"[PASS] {header}") # Print the header that is present
        print(f"       {response.headers[header]}\n") # Print the value in dict of the header
        passed += 1 # Increment the count of headers that are present
    else:
        print(f"[FAIL] {header}") # Print the header that is not present
        print(f"       Header not present\n") # Print the message that the header is not present

print("=" * 50) # Print a separator line
print(f"Score: {passed}/{len(HEADERS_TO_CHECK)} headers present") # Print the score


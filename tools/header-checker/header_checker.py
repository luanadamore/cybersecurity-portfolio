# header_checker.py
# Checks HTTP security headers on a given URL
# Usage: python header_checker.py <url>

import sys #Access to command-line arguments 
import requests #HTTP requests

if len(sys.argv) < 2: # sys.argv is a list of command-line arguments
    print("Usage: python header_checker.py <url>")
    sys.exit(1) # Exit the program with an error code

url = sys.argv[1] # The URL to check

HEADERS_TO_CHECK = {
    "Strict-Transport-Security": "MISSING — site vulnerable to HTTPS downgrade attacks",
    "Content-Security-Policy":   "MISSING — site vulnerable to XSS script injection",
    "X-Frame-Options":           "MISSING — site vulnerable to clickjacking attacks",
    "X-Content-Type-Options":    "MISSING — site vulnerable to MIME sniffing attacks",
    "Referrer-Policy":           "MISSING — sensitive URLs may leak to third parties",
}  # dictionary of headers to check, with a message for each header

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=True, timeout=10) # Send a GET request to the URL, with a user agent, allow redirects, and a timeout of 10 seconds
    response.raise_for_status() # Raise an exception for 4xx/5xx status codes
except requests.exceptions.RequestException as e: # If an exception occurs, print the error and exit the program
    print(f"Error: {e}")
    sys.exit(1) # Exit the program

print(f"\nChecking: {url}")
print("=" * 50) # Print a separator line

passed = 0 # Count the number of headers that are present

for header, fail_message in HEADERS_TO_CHECK.items():
    if header in response.headers:
        print(f"[PASS] {header}") # Print the header that is present    
        print(f"       {response.headers[header]}\n") # Print the value of the header
        passed += 1 # Increment the count of headers that are present
    else:
        print(f"[FAIL] {header}") # Print the header that is not present
        print(f"       {fail_message}\n") # Print the message that the header is not present, from the dictionary

print("=" * 50) # Print a separator line
print(f"Score: {passed}/{len(HEADERS_TO_CHECK)} headers present") # Print the score


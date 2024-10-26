#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

 - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
   <status code> <file size> (if the format is not this one, the line
   must be skipped)
 - After every 10 lines and/or a keyboard interruption (CTRL + C),
   print these statistics from the beginning:
 - Total file size: File size: <total size>
 - where <total size> is the sum of all previous <file size> (see input
   format above)
 - Number of lines by status code:
     - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
     - If a status code doesn’t appear or is not an integer, don’t print
       anything for this status code
     - format: <status code>: <number>
     - status codes should be printed in ascending order
"""
import re
import sys
import signal


total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}


# Finds the total file size
def print_metrics():
    """
    Prints the number of lines for each status_code
    """
    print(f"File size: {total_size}")
    for status_code, count in status_codes_count.items():
        if count == 0:
            continue
        print(f"{status_code}: {count}")


# Handle keyboard interruption
def signal_handler(sig, frame):
    """ Handles keyboard interruption signal """
    print_metrics()
    sys.exit(0)


# Attach signal handler to SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

# Define regex pattern to verify input format
log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \['
    r'(.*?)\] "GET (.*?)" (\d{3}) (\d+)$'
)

# Main code
line_count = 0

# read input line by line
while True:
    line = sys.stdin.readline()  # does not store in memory
    if not line:
        break

    # strip trailing and leading whitespaces
    line = line.strip()

    # Verify format of the read line
    match = log_pattern.match(line)
    if not match:
        continue  # skip line

    # Extract status code and file size
    try:
        status_code = int(match.group(4))
        size = int(match.group(5))
    except ValueError:
        continue  # skip if parsing fails

    # update counters
    total_size += size
    if status_code in status_codes_count:
        status_codes_count[status_code] += 1

    line_count += 1

    # Print output every time line count is 10
    if line_count % 10 == 0:
        print_metrics()

# End of loop -- print output
if line_count % 10 != 0:
    print_metrics()

#!/usr/bin/env python3
import sys
import re
from collections import defaultdict

# Define a regex pattern for matching the input log format
log_pattern = re.compile(
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - \[(?P<date>[^\]]+)\] '
    r'"GET (?P<path>/[^ ]+) HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)$'
)


def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()  # Remove leading/trailing whitespace
            match = log_pattern.match(line)

            if match:
                status = match.group('status')
                size = int(match.group('size'))

                total_size += size  # Accumulate the total file size
                status_codes[status] += 1

                line_count += 1

                # Print metrics after every 10 lines
                if line_count % 10 == 0:
                    print_metrics(total_size, status_codes)

        # Print final metrics if the end of input is reached
        print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print_metrics(total_size, status_codes)


def print_metrics(total_size, status_codes):
    print(f'File size: {total_size}')

    # Print status codes in ascending order
    for code in sorted(status_codes.keys()):
        print(f'{code}: {status_codes[code]}')


if __name__ == '__main__':
    main()

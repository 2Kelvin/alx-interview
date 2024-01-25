#!/usr/bin/python3
'''Log parsing'''
import sys
import re

totalFileSize = 0
statusCodeCounts = {}
lineCount = 0

while True:
    try:
        userLineInput = sys.stdin.readline()
        inputFormat = (
            r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \["
            r"(.*?)"
            r"\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$"
        )
        matching = re.match(inputFormat, userLineInput)

        if matching:
            lineCount += 1
            file_size = int(matching.group(4))
            totalFileSize += file_size
            # Convert status code to integer
            status_code = int(matching.group(3))
            statusCodeCounts[status_code] = statusCodeCounts.get(
                status_code, 0) + 1

            if lineCount % 10 == 0 or KeyboardInterrupt:
                print(f'File size: {totalFileSize}')
                # Print status codes in ascending order
                for code in sorted(statusCodeCounts):
                    print(f'{code}: {statusCodeCounts[code]}')
        else:
            continue  # Skip lines that don't match the format

    except KeyboardInterrupt:
        break  # Exit the loop on Ctrl+C

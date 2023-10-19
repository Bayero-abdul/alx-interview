#!/usr/bin/python3
"""0. Log parsing """


import sys


line_count = 0
total_size = 0

possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_codes = {}

try:
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break

        line_args = line.split(' ')
        file_size = line_args[-1]
        status_code = line_args[-2]

        # skip line if of not of this format
        # <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
        # <status code> <file size>
        if len(line_args) != 9:
            continue

        line_count += 1
        total_size += int(file_size)

        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        if line_count % 10 == 0:
            line_count = 0

            print('File size: {}'.format(total_size))
            sorted_codes = dict(
                sorted(
                    status_codes.items(),
                    key=lambda item: item[0]))
            for k, v in sorted_codes.items():
                if k in possible_codes:
                    print('{}: {}'.format(k, v))

except KeyboardInterrupt:
    print('File size: {}'.format(total_size))
    sorted_codes = dict(sorted(status_codes.items(), key=lambda item: item[0]))
    for k, v in sorted_codes.items():
        if k in possible_codes:
            print('{}: {}'.format(k, v))

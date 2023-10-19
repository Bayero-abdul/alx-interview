#!/usr/bin/python3
"""0. Log parsing """


import sys
import re


if __name__ == "__main__":
    line_count = 0
    total_size = 0

    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_codes = {}

    regex = (r'\d+.\d+.\d+.\d+\s?-\s?\[\d+-\d+\d+-\d+ \d+:\d+:\d+\.\d+\] '
             r'\"GET \/projects\/260 HTTP\/1\.1\" (\d+) \d+')

    # pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
    # r'\d{2}:\d{2}:\d{2}\.\d+\] \"GET \/projects\/260 HTTP\/1\.1\" \d+ \d+'

    try:
        for line in sys.stdin:  
            match = re.search(regex, line.strip())
            if match:
                line_args = line.strip().split()
                file_size = line_args[-1]
                status_code = line_args[-2]

                line_count += 1
                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

                status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if line_count == 10:
                line_count = 0

                print('File size: {}'.format(total_size))
                sorted_codes = dict(
                    sorted(
                        status_codes.items(),
                        key=lambda item: item[0]))
                for k, v in sorted_codes.items():
                    if k in possible_codes:
                        print('{}: {}'.format(k, v))
            sys.stdin.flush()
    except (KeyboardInterrupt, EOFError) as e:
        print()
    finally:
        print('File size: {}'.format(total_size))
        sorted_codes = dict(
            sorted(
                status_codes.items(),
                key=lambda item: item[0]))
        for k, v in sorted_codes.items():
            if k in possible_codes:
                print('{}: {}'.format(k, v))

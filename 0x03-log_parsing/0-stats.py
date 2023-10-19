#!/usr/bin/python3
"""0. Log parsing """


import sys
import re


if __name__ == "__main__":
    line_count = 0
    total_size = 0

    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0}

    pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
    r'\d{2}:\d{2}:\d{2}\.\d+\] \"GET \/projects\/260 HTTP\/1\.1\" \d+ \d+'

    try:
        for line in sys.stdin:
            match = re.search(pattern, line.strip())
            if match:
                line_args = line.strip().split()
                file_size = line_args[-1]
                status_code = line_args[-2]

                line_count += 1
                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

                if status_code in status_codes:
                    status_codes[status_code] += 1

                if line_count == 10:
                    line_count = 0

                    print('File size: {}'.format(total_size))
                    for code, count in status_codes.items():
                        if count > 0:
                            print('{}: {}'.format(code, count))

            sys.stdin.flush()
    except (KeyboardInterrupt, EOFError) as e:
        print()
    finally:
        print('File size: {}'.format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f'{code}: {status_codes[code]}')
        sys.stdin.flush()

#!/usr/bin/python3

'''
0-stats script
Reads stdin line by line and computes metrics
'''

import sys
import re


if __name__ == '__main__':
    nlr = 0  # number of lines read
    sum_size = 0  # sum of file sizes
    codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    regex = (r'\d+.\d+.\d+.\d+\s?-\s?\[\d+-\d+\d+-\d+ \d+:\d+:\d+\.\d+\] '
             r'\"GET \/projects\/260 HTTP\/1\.1\" (\d+) \d+')

    try:
        for line in sys.stdin:
            if re.search(regex, line.strip()):
                nlr += 1
                line = line.strip().split()
                code, file_size = line[-2], line[-1]
                try:
                    sum_size += int(file_size)
                except ValueError as v:
                    pass
                if code in codes:
                    codes[code] += 1
            if nlr == 10:
                nlr = 0
                print(f'File size: {sum_size}')
                for c in codes:
                    if codes[c] > 0:
                        print(f'{c}: {codes[c]}')
            sys.stdin.flush()
    except (KeyboardInterrupt, EOFError) as e:
        print()
    finally:
        print(f'File size: {sum_size}')
        for c in sorted(codes.keys()):
            if codes[c] > 0:
                print(f'{c}: {codes[c]}')
        sys.stdin.flush()
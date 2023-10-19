# 0x03. Log Parsing

## Project Overview

The Log Parsing project is part of the curriculum at Holberton School. It involves writing a script in Python that reads input data from the standard input (stdin) line by line and computes specific metrics. The script is designed to process log data with a particular format, skip lines that don't match the format, and print statistics as specified in the tasks section.

## Getting Started

To get started with this project, follow these steps:

1. Clone the project repository from [GitHub](https://github.com/alx-interview/0x03-log_parsing) to your local machine.

2. Ensure you have Python 3.4.3 or later installed on your system.

3. Review the project tasks and requirements to understand what needs to be implemented.

## Running the Tasks

The project consists of two main files:

- `0-generator.py`: This script generates random log data and sends it to the standard output (stdout). You can use this script to generate sample data for testing.

- `0-stats.py`: This script reads log data from the standard input (stdin) and computes metrics based on the specified format. It processes the data and prints statistics as per the defined rules.

### Example Usage:

```bash
./0-generator.py | ./0-stats.py
```

This command runs the log data generator and pipes its output to the log parsing script, which computes and prints statistics.

## Project Structure

- `0-generator.py`: The script responsible for generating random log data.

- `0-stats.py`: The main log parsing script that processes and computes metrics for the log data.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the project folder, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

### Tasks

**0. Log Parsing (mandatory)**

Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:

- Total file size: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>` as per the input format)

- Number of lines by status code:

  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500

  - If a status code doesn’t appear or is not an integer, don’t print anything for this status code

  - Format: `<status code>: <number>` (status codes should be printed in ascending order)

  - In this sample, you will have random value - it’s normal to not have the same output as this one.


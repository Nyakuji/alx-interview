#!/usr/bin/python3
"""Log parsing"""
import sys


def print_stats(total_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    """Parses a single line"""
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        return total_size, status_codes
    except (ValueError, IndexError):
        return total_size, status_codes


def log_parsing():
    """Main function"""
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line_count != 0 and line_count % 10 == 0:
                print_stats(total_size, status_codes)
            total_size, status_codes = parse_line(
                line, total_size, status_codes)
            line_count += 1

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    log_parsing()

#!/usr/bin/env python3
"""
stdin passthrough hook script.
Reads stdin and outputs it directly to stdout.
"""
import sys

def main():
    # Read all stdin
    stdin_data = sys.stdin.read()

    # Output to stdout (passthrough)
    print(stdin_data, end='')

    # Exit with success code
    sys.exit(0)

if __name__ == '__main__':
    main()

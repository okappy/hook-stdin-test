#!/usr/bin/env python3
"""
stdin passthrough hook script.
Reads stdin and outputs it to both stderr (user display) and stdout (Claude context).
"""
import sys
import json

def main():
    # Read all stdin
    stdin_data = sys.stdin.read()

    # Output to stderr for user to see on screen
    print(f"[Hook] Received: {stdin_data[:200]}..." if len(stdin_data) > 200 else f"[Hook] Received: {stdin_data}", file=sys.stderr)

    # Output to stdout (passthrough to Claude)
    print(stdin_data, end='')

    # Exit with success code
    sys.exit(0)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
stdin passthrough hook script.
Reads stdin and outputs it with systemMessage for user display.
"""
import sys
import json

def main():
    # Read all stdin
    stdin_data = sys.stdin.read()

    # Truncate for display
    display_data = stdin_data[:200] + "..." if len(stdin_data) > 200 else stdin_data

    # Output JSON with systemMessage for user display
    output = {
        "systemMessage": f"[Hook] Received: {display_data}"
    }
    print(json.dumps(output))

    # Exit with success code
    sys.exit(0)

if __name__ == '__main__':
    main()

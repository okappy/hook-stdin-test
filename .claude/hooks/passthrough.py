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

    # Parse input JSON to extract event name
    try:
        input_json = json.loads(stdin_data)
        event_name = input_json.get("hook_event_name", "unknown")
    except json.JSONDecodeError:
        event_name = "parse_error"

    # Log to file for debugging
    with open("/tmp/hook-debug.log", "a") as f:
        f.write(f"Event: {event_name}\n")
        f.write(f"Input: {stdin_data[:500]}\n")
        f.write("-" * 50 + "\n")

    # Output JSON with systemMessage for user display
    output = {
        "systemMessage": f"[Hook] Event: {event_name}"
    }
    print(json.dumps(output))

    # Exit with success code
    sys.exit(0)

if __name__ == '__main__':
    main()

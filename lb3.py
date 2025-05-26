#!/usr/bin/env python3
import sys
import math

def main():
    try:
        C = float(sys.stdin.read().strip())
        if C < 0:
            raise ValueError("It is impossible to find the root of a negative number")
        result = math.sqrt(C)

        with open("output.txt", "w") as output_file:
            output_file.write(f"Square root of {C} is {result}\n")
        with open("logs.txt", "a") as log_file:
            log_file.write(f"C = {C}, sqrt(C) = {result}\n")

    except ValueError as e:
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

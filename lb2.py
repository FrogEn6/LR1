#!/usr/bin/env python3
import random
import sys

def main():
    try:
        A = int(sys.stdin.readline())
        B = random.randint(-10, 10)
        result_dividing_A_by_B = A / B
        print(result_dividing_A_by_B)

        if B == 0:
            raise ZeroDivisionError("B = 0: division by zero is not allowed")
        
        with open("logs.txt", "a") as log_file:
            log_file.write(f"B = {B}, C = {result_dividing_A_by_B}\n")

    except Exception as e:
        print(f"Error: {str(e)}", file = sys.stderr)

if __name__ =="__main__":
    main()

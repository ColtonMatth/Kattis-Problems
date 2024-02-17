#Name: Colton Matthews
#File: smallestMult.py
#Date: 11/7/2022

import sys
from math import gcd

def lcm_two(a, b):
    return a * b // gcd(a, b)

def lcm(many):
    try: 
        a = next(many)
        b = next(many)
        current = lcm_two(a, b)
    except StopIteration:
        return a
    while True:
        try:
            current = lcm_two(current, next(many))
        except StopIteration:
            return current

def main():
    for line in sys.stdin:
        print(lcm(map(int, line.split())))

if __name__ == "__main__":
    main()
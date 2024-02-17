#Name: Colton Matthews
#File: zagrade.py
#Date: 10/16/2022

from collections import deque
from itertools import combinations

def all_possible(original, pairs):
    n = len(pairs)
    collect = set()
    for i in range(1, n + 1):
        for r in combinations(pairs, i):
            remove = {index for pair in r for index in pair}
            collect.add(''.join(c for i, c in enumerate(original) if i not in remove))
    return sorted(collect)

def main():
    stack = deque()
    pairs = []
    original = input()
    for i, x in enumerate(original):
        if x == '(':
            stack.append(i)
        elif x == ')':
            pairs.append((stack.pop(), i))
    print('\n'.join(all_possible((original), pairs)))


if __name__ == "__main__":
    main()
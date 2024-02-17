#Name: Colton Matthews
#File: anagramCounting.py
#Date: 11/8/2022

import sys

factorial = {0: 1}
for i in range(1, 101):
    factorial[i] = i * factorial[i - 1]

for _inp in sys.stdin:
    word = str(_inp.split()[0])
    occurrence = {}
    for char in word:
        if ord(char) in occurrence:
            occurrence[ord(char)] += 1
        else:
            occurrence[ord(char)] = 1
    value = factorial[len(word)]
    for i in occurrence:
        value = value // factorial[occurrence[i]]
    print(value)
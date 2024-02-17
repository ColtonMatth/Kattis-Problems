#Name: Colton Matthews
#File: cookieSelection.py
#Date: 10/8/2022

from sys import stdin

from heapq import heappop, heappush

class MaxHeap:
    def __init__(self):
        self.c = []

    def __len__(self):
        return len(self.c)
    
    def push(self, n):
        heappush(self.c, -n)
    
    def head(self):
        return -self.c[0]
    
    def pop(self):
        return -heappop(self.c)


class MinHeap:
    def __init__(self):
        self.c = []
    
    def __len__(self):
        return len(self.c)

    def push(self, n):
        heappush(self.c, n)

    def head(self):
        return self.c[0]

    def pop(self):
        return heappop(self.c)

class medianArray:
    def __init__(self):
        self.maximum = MaxHeap()
        self.minimum = MinHeap()

    def add(self, n):
        if not self.maximum:
            self.maximum.push(n)
        else:
            if n > self.maximum.head():
                self.minimum.push(n)
                if len(self.minimum) > len(self.maximum):
                    self.maximum.push(self.minimum.pop())
            else:
                self.maximum.push(n)
                if len(self.maximum) > len(self.minimum) + 1:
                    self.minimum.push(self.maximum.pop())
    
    def median(self):
        if len(self.maximum) == len(self.minimum):
            return self.minimum.pop()
        else:
            return self.maximum.pop()
    

def main():
    ans = medianArray()
    for line in stdin:
        if line[0] == '#':
            print(ans.median())
        else:
            ans.add(int(line))

if __name__ == "__main__":
    main()
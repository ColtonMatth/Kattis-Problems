#Name: Colton Matthews
#File: baloni.py
#Date: 9/19/2022

from collections import defaultdict

def main():
    n = defaultdict(lambda: 0)
    input()
    total_arrow = 0 #total number of times to shoot an arrow, to get all balloons
    for h in map(int, input().split()): #input and iterate the array of n
        if n[h+1] > 0: 
            #if h is greater than 0, then h-1 for n[h+1]
            n[h+1] -= 1
        else: 
            #if h is equal to 0 then add total by one, and then iterate the
            # next element of n[h]
            total_arrow += 1
        n[h] += 1
    print(total_arrow)

if __name__ == "__main__":
    main() 
#Name: Colton Matthews
#File: DAsort.py
#Date: 10/11/2022

def sort(arr):
    low, min_move, mtm_i, to_move = (1000000001, 1000000001, len(arr), set())

    #Finding all of the elements that are smaller move to the right
    for i, c in enumerate(reversed(arr)):
        if c > low:
            to_move.add(len(arr) - 1 - i)
            if c <= min_move:
                min_move = c
                mtm_i = len(arr) - 1 - i
        else:
            low = c
    
    #A special case that some smallest element are already at the end
    if arr[-1] == min_move:
        return len(to_move)

    #Any element larger than any smaller elements will move to the right
    #Since the smallest elements are already moved to the right in the 
    #reversed array, although it would create an inversion between the 
    #current element and any larger element move to the right.
    for i, c in enumerate(arr[mtm_i + 1:]):
        if c > min_move:
            to_move.add(mtm_i + 1 + i)

    return len(to_move)

def main():
    for i in range(int(input())):
        _,c = map(int,input().split())
        lis = []
        for _ in range(c // 10 + (1 if c % 10 > 0 else 0)):
            lis.extend(map(int,input().split()))
        ops = sort(lis)
        print(f'{i+1} {ops}')

if __name__ == "__main__":
    main()
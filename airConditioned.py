#Name: Colton Matthews
#File: airConditioned.py
#Date: 10/14/2022

def rooms(arr):
    counter = 0
    while arr:
        counter += 1
        a, b = arr.pop()
        while arr and (a <= arr[-1][0] <= b or a <= arr[-1][1] <= b):
            _a, _b = arr.pop()
            a = max(a, _a)
            b = min(b, _b)
    return counter

def main():
    n = int(input())
    arr = sorted((tuple(map(int, input().split())) for _ in range(n)), reverse = True)
    print(rooms(arr))

if __name__ == "__main__":
    main()

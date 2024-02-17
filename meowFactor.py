#Name: Colton Matthews
#File: meowFactor.py
#Date: 11/4/2022

def meow(n):
    for i in range(128, 0, -1):
        z = i**9
        if z > n:
            continue
        if n % z == 0:
            return i
    return 1

def main():
    print(meow(int(input()))) 

if __name__ == "__main__":
    main()
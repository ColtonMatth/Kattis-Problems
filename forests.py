#Name: Colton Matthews
#File: forests.py
#Date: 10/16/2022

def main():
    p,t = map(int, input().split())
    possibilities = [set() for _ in range(p)]
    try:
        for _ in range(p * t):
            _p,_t = map(int, input().split())
            possibilities[_p-1].add(_t)
    except EOFError:
        pass
    print(len({frozenset(s) for s in possibilities}))

if __name__ == '__main__':
    main()
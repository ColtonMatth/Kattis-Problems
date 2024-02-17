#Name: Colton Matthews
#File: fallingapp.py
#Date: 9/23/2022

def column_sim(r, c, table):
    while r > 0:
        if table[r][c] == '.':
            offset = 0
            _r = r - 1
            while True:
                if _r < 0:
                    return
                if table[_r][c] == '#':
                    r = _r - 1
                    break
                elif table[_r][c] == 'a':
                    table[_r][c] = '.'
                    table[r-offset][c] = 'a'
                    offset += 1
                _r -= 1
        else:
            r -= 1

def simulate(r, c, table):
    for i in range(c):
        column_sim(r-1, i, table)

def main():
    R, C = map(int, input().split())
    table = [list(input()) for _ in range(R)]
    simulate(R, C, table)
    print('\n'.join(''.join(char for char in row) for row in table))

if __name__ == "__main__":
    main()
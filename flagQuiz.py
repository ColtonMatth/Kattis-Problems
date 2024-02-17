#Name: Colton Matthews
#File: flagQuiz.py
#Date: 10/17/2022

def fill_dist(n):
    difference = [[0] * n for _ in range(n)]
    option = []
    for i in range(n):
        option.append(input().split(', '))
        for j in range(i):
            data = sum(a != b for a, b in zip(option[i], option[j]))
            difference[i][j] = data
            difference[j][i] = data
    return difference, option

def find_best(difference):
    least, least_element = 2147483647, []
    for i, row in enumerate(difference):
        if (s := max(row)) == least:
            least_element.append(i)
        elif s < least:
            least_element = [i]
            least = s
    return least_element

def main():
    input()
    n = int(input())
    difference, option = fill_dist(n)
    best = find_best(difference)
    print('\n'.join((', '.join(option[i]) for i in best)))

if __name__ == "__main__":
    main()

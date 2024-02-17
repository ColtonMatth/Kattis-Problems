#Name: Colton Matthews
#File: teacherEval.py
#Date: 10/13/2022

def get_score(n, s, p):
    a = n * p - s
    b = 100 - p
    d, m = divmod(a, b)
    return d if m else d - 1

def add_test(n, s, p):
    if p == 100:
        return 'impossible' if 100 * n != s else 0
    k = get_score(n, s, p) 
    s += 100 * k
    if (expect_sum := (n + k) * p) == s:
        return k
    for i in range(1, 100):
        if s + i == expect_sum:
            return k + 1
    return 'impossible'

def main():
    (n, p), s = map(int, input().split()), sum(map(int, input().split()))
    print(add_test(n, s, p))


if __name__ == "__main__":
    main()

#Name: Colton Matthews
#File: basicprog2.py
#Data: 9/22/2022

from collections import Counter

def t1(n, data):
    sets = set(data)
    for i in range(1, 7777):
        if i in sets and 7777 - i in sets:
            return ('Yes',)
    return ('No',)

def t2(n, data):
    if len(set(data)) == n:
        return ('Unique',)
    else:
        return ('Contains duplicate',)
    
def t3(n, data):
    a, b = Counter(data).most_common(1)[0]
    return (a,) if b > n/2 else (-1,)
    
def t4(n, data):
    data_sorted = sorted(data)
    if len(data_sorted) % 2 == 1:
        return (data_sorted[len(data_sorted)//2],)
        
    else:
        return data_sorted[len(data_sorted)//2 - 1: len(data_sorted)//2 + 1]
        
def t5(n, data):
    return sorted(filter(lambda z: 99 < z < 1000, data))

def print_result(n, t, data):
    return [t1, t2, t3, t4, t5][t - 1](n, data)

def main():
    print(*print_result(*map(int,input().split()),map(int,input().split())))

if __name__ == "__main__":
    main()
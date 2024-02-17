#Name: Colton Matthews
#File: basicprog1.py
#Date: 9/11/2022

from itertools import islice

#by ignoring the content, print 7 if t = 1
def t_1(n, data):
    return 7

#checking the equality of the first two elements
def t_2(n, data):
    a, b = islice(data, 0, 2)
    if a > b:
        return 'Bigger'
    elif a == b:
        return 'Equal'
    else:
        return 'Smaller'

#find the median of the first three elements
def t_3(n, data):
    return sorted(islice(data, 0, 3))[1]

#find the sum of the array
def t_4(n, data):
    return sum(data)

#find the sum of even numbers
def t_5(n, data):
    return sum(i for i in data if i % 2 == 0)

#Converting the sequence of int to char by using modulo 26 and ASCII digits
def t_6(n, data):
    return ''.join(chr(97 + i % 26) for i in data)


def t_7(n, data):
    data_list = list(data)
    #visited variable will check if the element has been checked 
    visited = [False]*n 
    i = 0
    while True:
        if i >= n: #if i is out of bounds of n
            return 'Out'
        if visited[i]: #if it leads to an infinite loop
            return 'Cyclic'
        if i == n-1: #if i reaches the end of the array
            return 'Done'
        visited[i] = True
        i = data_list[i]

def main():
    n,t = map(int,input().split())
    data = map(int,input().split())
    print([t_1,t_2,t_3,t_4,t_5,t_6,t_7][t-1](n,data))

if __name__ == "__main__":
    main()
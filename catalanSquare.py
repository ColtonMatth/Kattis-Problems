#Name: Colton Matthews
#File: catalanSquare.py
#Date: 11/8/2022

n = int(input())
catalan = {0:1}
for i in range(n + 1):
    catalan[i + 1] = catalan[i] * (4 * i + 2) // (i + 2)
print(catalan[n + 1])

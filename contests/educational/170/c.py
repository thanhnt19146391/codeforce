import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

for _  in range(int(input())):
    n, k = inp(int)
    a = inp(int)
    a.sort()
    res = 0
    j = 0
    for i in range(n):
        j = max(i, j)
        while j + 1 < n and a[j + 1] - a[j] <= 1 and a[j + 1] - a[i] < k:
            j += 1
        res = max(res, j - i + 1)
    print(res)
    
            


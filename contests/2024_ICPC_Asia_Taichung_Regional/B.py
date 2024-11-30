import sys
import math

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

def find_k(n):
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if mid * (mid + 1) <= n:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


for _ in range(int(input())):
    w, b = inp(int)
    print(find_k((w + b) * 2))

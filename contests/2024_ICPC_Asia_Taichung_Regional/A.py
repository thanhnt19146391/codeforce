import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

a, b, c, d = inp(int)
res = 15 - a - b - c - d
print(res)
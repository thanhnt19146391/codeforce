import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

def solve():
    t = int(input())
    
    for _ in range(t):
        n, m, q = inp(int)
        a = array('i', inp(int))
        b = array('i', inp(int))

        # Array c using for marking member who presented slide
        c = array('i', (n + 1) * [0])
        res = 1
        j = 0
        for i in range(len(b)):
            if j == len(a):
                break
            elif (a[j] == b[i]):
                c[a[j]] = 1
                j += 1
            elif (c[b[i]]):
                pass
            else:
                res = 0
                break
        print('YA' if res else 'TIDAK')

if __name__ == '__main__':
    solve()

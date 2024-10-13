import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

def check0():
    # c: array using for marking member who presented slide
    # if member 'x' presented slide, c[x] = 1, 
    # otherwise c[x] = 0
    c = array('i', (n + 1) * [0])

    # res: state the presentation that is either
    # good or not at the instant. Initially, 'res' was set 1.
    res = 1

    # j: the index of the current member who is front of lineup. 
    j = 0

    for i in range(len(b)):
        if j == len(a): # All member presented slide and was pending 
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

def check1():
    pass

def solve():
    t = int(input())
    global n, m, q, a, b
    for _ in range(t):
        n, m, q = inp(int)
        a = array('i', inp(int))
        b = array('i', inp(int))
        check0()
        for _ in range(q):
            s, t = inp(int)
            check1()



        

if __name__ == '__main__':
    solve()

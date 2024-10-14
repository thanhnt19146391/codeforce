import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

def check1():
    global first, ans
    # print(first)
    res = 1
    for i in range(n - 1):
        if first[a[i]] > first[a[i + 1]]:
            res = 0
            break
    ans.append('YA' if res else 'TIDAK')

def _get_first_position(member: int):
    global sets, m
    pos_set = sets[member]
    if len(pos_set) == 0:
        return m
    return array('i', pos_set)[0]

def solve():
    t = int(input())
    global n, m, q, a, b, ans
    ans = []
    for _ in range(t):
        n, m, q = inp(int)
        a = array('i', inp(int))
        b = array('i', inp(int))
        global sets
        # sets[x] : the set containning the indices of occurrence of member x
        sets = [set() for _ in range(n + 1)]
        for i in range(m):
            sets[b[i]].add(i)
        global first
        first = array('i', (n + 1) * [0])
        for x in a:
            first[x] = _get_first_position(member = x)
        check1()

        for _ in range(q):
            s, t = inp(int)
            pos = s - 1
            member = b[pos]
            sets[t].add(pos)
            sets[member].remove(pos)
            # print(sets)
            first[t] = _get_first_position(member = t)
            first[member] = _get_first_position(member = member)
            check1()
            b[pos] = t
    print('\n'.join([x for x in ans]))

if __name__ == '__main__':
    solve()

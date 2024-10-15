import sys
from array import array
import heapq

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

def check1():
    global first, ans_list
    # print(first)
    res = 1
    for i in range(n - 1):
        if first[a[i]] > first[a[i + 1]]:
            res = 0
            break
    ans = 'YA' if res else 'TIDAK'
    ans_list.append(ans)

def _get_first_position(member: int):
    global pos_list, m, sets
    member_pos = pos_list[member]
    ignore_pos_set = sets[member]
    while True:
        if len(member_pos) == 0:
            return m
        if member_pos[0] in ignore_pos_set:
            heapq.heappop(member_pos)
        else:
            return member_pos[0]

def solve():
    t = int(input())
    global n, m, a, b, ans_list
    ans_list = []
    for _ in range(t):
        n, m, q = inp(int)
        a = array('i', inp(int))
        b = array('i', inp(int))
        global pos_list
        pos_list = [[] for _ in range(n + 1)]
        global first
        first = array('i', [m for _ in range(n + 1)])
        for i in range(m):
            heapq.heappush(pos_list[b[i]], i)
            if first[b[i]] == m:
                first[b[i]] = i
        check1()
        
        global sets
        sets = [set() for _ in range(n + 1)]
        for _ in range(q):
            s, t = inp(int)
            new_pos = s - 1
            old_member = b[new_pos]
            heapq.heappush(pos_list[t], new_pos)
            sets[old_member].add(new_pos)
            first[t] = _get_first_position(member = t)
            first[old_member] = _get_first_position(member = old_member)
            b[new_pos] = t
            check1()
            
    print('\n'.join([x for x in ans_list]))

if __name__ == '__main__':
    solve()

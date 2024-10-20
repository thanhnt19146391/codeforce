import sys
from array import array

input = lambda: sys.stdin.buffer.readline().decode().rstrip()
inp = lambda dtype: [dtype(x) for x in input().split()]

for _  in range(int(input())):
    n, k = inp(int)
    lst_a = inp(int)
    lst_a.sort()
    a = array('i', lst_a)
    # print(n, k, a)
    b = array('i', [])
    cnt = array('i', [])
    break_point = array('i', [])
    j = 0
    for i in range(n):
        if len(b) == 0:
            b.append(a[i])
            cnt.append(0)
        if a[i] == b[j]:
            cnt[j] += 1
        else:
            b.append(a[i])
            cnt.append(1)
            if a[i] != b[j] + 1:
                
            j += 1
    # print(b, '\n', cnt)

    m = len(b)
    sum = array('i', [])
    for i in range(m):
        if len(sum) == 0:
            sum.append(b[i])
        else:
            sum.append(sum[i-1] + b[i])
        

    sum.append(0)


            


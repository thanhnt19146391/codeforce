from array import array
import heapq
import random
s = set()
h = []
for _ in range(10):
    num = random.randint(0, 100)
    s.add(num)
    heapq.heappush(h, num)


print(s)
a = array('i', s)
print(a)
for _ in range(10):
    print("before: ", h)
    first = heapq.heappop(h)
    print('first: ', first)
    print("after: ", h)
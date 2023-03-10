# from sys import stdin
# from heapq import heappush, heappop
# input = stdin.readline

'''
t = int(input())

for _ in range(t):
    _heap = []
    k = int(input())
    for _ in range(k):
        culc, num = input().split()
        if culc == 'I':
            heappush(_heap, int(num.strip()))

        elif culc == 'D':
            if _heap:
                if num == '-1':
                    heappop(_heap)

                elif num == '1':
                    _heap.pop()
    if _heap:
        if len(_heap) != 1:
            print(_heap.pop(), heappop(_heap))
        else:
            print(_heap[0], _heap[0])
    else:
        print("EMPTY")

_heap.pop()이 최대를 반환하지 않음.
heappush코드를 살펴보면 앎.

def _siftdown(_heap, startpos, pos):
    newitem = _heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = _heap[parentpos]
        if newitem < parent:
            _heap[pos] = parent
            pos = parentpos
            continue
        break
    _heap[pos] = newitem

def heappush(_heap, item):
    """Push item onto _heap, maintaining the _heap invariant."""
    _heap.append(item)
    _siftdown(_heap, 0, len(_heap)-1)
'''
'''
t = int(input())

for _ in range(t):
    max_heap, min_heap = [], []
    k = int(input())
    for i in range(k):
        culc, num = input().split()
        if culc == 'I':
            num = int(num.strip())
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, i))

        elif culc == 'D':
            if num == '-1':
                if min_heap:
                    value, index = heappop(min_heap)
                    max_heap.remove((-value, index))
            elif num == '1':
                if max_heap:
                    value, index = heappop(max_heap)
                    min_heap.remove((-value, index))

    if min_heap:
        if len(min_heap) != 1:
            print(-heappop(max_heap)[0], heappop(min_heap)[0])
        else:
            print(max_heap[0], min_heap[0])
    else:
        print("EMPTY")
'''
from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

max_q = []
min_q = []

t = int(input())
for _ in range(t):
    k = int(input())
    max_q, min_q = [], []
    visited = [False] * (k + 1)

    for i in range(k):
        calcs, num = input().split()

        if calcs == 'I':
            visited[i] = True
            heappush(max_q, (-int(num), i))
            heappush(min_q, (int(num), i))

        elif calcs == 'D':
            if num == '1':
                while max_q and not visited[max_q[0][1]]:
                    heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heappop(max_q)

            elif num == '-1':
                while min_q and not visited[min_q[0][1]]:
                    heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heappop(min_q)
    while min_q and not visited[min_q[0][1]]:
        heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heappop(max_q)
    if min_q:
        print(f'{-max_q[0][0]} {min_q[0][0]}')
    else:
        print("EMPTY")
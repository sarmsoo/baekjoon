from heapq import heappush, heappop
from sys import stdin

input = stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    i = int(input().strip())

    if i == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, i)
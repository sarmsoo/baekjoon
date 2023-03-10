from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

n = int(input())
heap = []
for _ in range(n):
    i = int(input())

    if i == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (-i, i))
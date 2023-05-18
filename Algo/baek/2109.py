from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
lectures = []

for _ in range(n):
    p, d = map(int, input().split())
    lectures.append((p, d))
lectures.sort(key=lambda x: x[1])

pq = []

for p, d in lectures:
    heappush(pq, p)

    if d < len(pq):
        heappop(pq)

print(sum(pq))
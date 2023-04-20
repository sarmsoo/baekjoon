from sys import stdin
from heapq import heappush, heappop, heapify
input = stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapify(cards)

for _ in range(m):
    first = heappop(cards)
    second = heappop(cards)
    sum_ = first + second
    heappush(cards, sum_)
    heappush(cards, sum_)

print(sum(cards))
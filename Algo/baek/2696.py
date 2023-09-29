from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

for _ in range(int(input())):
    m = int(input())
    seq = []
    for _ in range(m // 10 + 1):
        tmp = list(map(int, input().split()))
        seq = seq + tmp

    lower = []
    upper = [seq[0]]
    answer = [seq[0]]
    for i in range(1, m):
        if seq[i] >= upper[0]:
            heappush(upper, seq[i])
        else:
            heappush(lower, -seq[i])

        if len(lower) > len(upper):
            heappush(upper, -heappop(lower))
        elif len(lower) + 1 < len(upper):
            heappush(lower, -heappop(upper))

        if (i + 1) % 2 != 0:
            answer.append((upper[0]))

    print(len(answer))
    for i in range(0, len(answer), 10):
        print(*answer[i:i+10])
from sys import stdin
import math
input = stdin.readline

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    answer = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        dist_start = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        dist_end = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)

        if dist_start < r and dist_end < r:
            continue
        if dist_start < r:
            answer += 1
            continue
        if dist_end < r:
            answer += 1
    print(answer)

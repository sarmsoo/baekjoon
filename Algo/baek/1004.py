from sys import stdin
import math
input = stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            continue
        if r1 != r2:
            print(0)
            continue

    if dist == r1 + r2:
        print(1)
        continue

    if dist > r1 + r2:
        print(0)
        continue

    if dist < r1 + r2:
        if dist < abs(r1 - r2):
            print(0)
            continue
        if dist == abs(r1 - r2):
            print(1)
            continue
        if dist > abs(r1 - r2):
            print(2)
            continue
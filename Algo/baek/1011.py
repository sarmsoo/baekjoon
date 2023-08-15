from sys import stdin
from itertools import count
input = stdin.readline


for _ in range(int(input())):
    x, y = map(int, input().split())
    l = y - x

    answer = 0
    m = 0
    for i in count(1):
        sum = i * (i + 1)
        if sum > l:
            l -= (i - 1) * i
            m = i - 1
            break

    answer += 2 * m
    while l > m + 1:
        l -= m + 1
        answer += 1

    if l == 0:
        print(answer)
    else:
        print(answer + 1)
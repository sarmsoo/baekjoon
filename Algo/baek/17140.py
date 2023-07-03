from sys import stdin
from collections import Counter
input = stdin.readline

def R():
    max_r = 0
    for i in range(len(a)):
        tmp = []
        tmp2 = []
        counter = Counter(a[i])
        for j in counter:
            if j == 0:
                continue
            tmp2.append((j, counter[j]))
        tmp2.sort(key=lambda x: (x[1], x[0]))

        if len(tmp2) > 50:
            tmp = tmp2[:50]

        for index, number in tmp2:
            tmp.append(index)
            tmp.append(number)

        max_r = max(max_r, len(tmp))
        a[i] = tmp
    for i in range(len(a)):
        for _ in range(len(a[i]), max_r):
            a[i].append(0)

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
a = [list(map(int, input().split())) for _ in range(3)]
time = 0
while True:
    if r < len(a) and c < len(a[0]):
        if a[r][c] == k:
            print(time)
            break
    if len(a) >= len(a[0]):
        R()
    else:
        a = list(map(list, zip(*a)))
        R()
        a = list(map(list, zip(*a)))

    time += 1
    if time > 100:
        print(-1)
        break
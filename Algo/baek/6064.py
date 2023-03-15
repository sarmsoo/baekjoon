from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    if x == y:
        print(x)
        continue

    flag = True
    for i in range(n + 1):
        if (m * i + x - y) % n == 0:
            print(m * i + x)
            flag = False
            break
    if flag:
        print(-1)
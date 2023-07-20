from sys import stdin
input = stdin.readline

n, l = map(int, input().split())

for i in range(l, 101):
    a = max(n // i - i // 2, 0)
    while True:
        tmp = i * a + (i - 1) * i // 2
        if tmp > n:
            break
        if tmp == n:
            print(*range(a, a + i))
            exit(0)
        a += 1
    if a == max(n // i - i // 2, 0):
        break
print(-1)
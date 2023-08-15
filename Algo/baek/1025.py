from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
table = [list(input().strip()) for _ in range(n)]

answer = -1
for i in range(n):
    for j in range(m):
        for rd in range(-n, n):
            for cd in range(-m, m):
                s = ""
                y, x = i, j
                if rd == 0 and cd == 0:
                    continue

                while 0 <= y < n and 0 <= x < m:
                    s += table[y][x]
                    if int(int(s) ** 0.5) ** 2 == int(s):
                        answer = max(answer, int(s))
                    y += rd
                    x += cd

print(answer)
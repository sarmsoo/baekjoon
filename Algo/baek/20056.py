from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
fireballs = []
graph = [[[] for _ in range(n)] for _ in range(n)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])

for _ in range(k):
    while fireballs:
        y, x, m, s, d = fireballs.pop()
        ny = (y + s * dy[d]) % n
        nx = (x + s * dx[d]) % n
        graph[ny][nx].append([m, s, d])

    for y in range(n):
        for x in range(n):
            if len(graph[y][x]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[y][x])
                while graph[y][x]:
                    m, s, d = graph[y][x].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                if sum_m // 5 == 0:
                    continue
                for d in nd:
                    fireballs.append([y, x, sum_m // 5, sum_s // cnt, d])

            elif len(graph[y][x]) == 1:
                fireballs.append([y, x] + graph[y][x].pop())

print(sum([fireball[2] for fireball in fireballs]))
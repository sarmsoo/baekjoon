from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

visited = [False] * len(chicken)

def metric():
    distance = 0
    for i in range(len(house)):
        h_y, h_x = house[i]
        tmp = 2 * n + 1
        for j in range(len(chicken)):
            if not visited[j]:
                 c_y, c_x = chicken[j]
                tmp = min(tmp, abs(h_y - c_y) + abs(h_x - c_x))

        distance += tmp
    return distance

result = 10 ** 5

def sol(start, cnt):
    global result
    if cnt == len(chicken) - m:
        result = min(result, metric())
        return

    for i in range(start, len(chicken)):
        if visited[i]:
            continue
        visited[i] = True

        sol(i + 1, cnt + 1)

        visited[i] = False

if len(chicken) > m:
    sol(0, 0)
    print(result)
else:
    print(metric())
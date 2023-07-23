from sys import stdin, maxsize
from math import sqrt
from heapq import heappush, heappop
input = stdin.readline

def dijkstra():
    pq = []
    dist[0] = 0
    heappush(pq, (0, 0))
    while pq:
        d, curr = heappop(pq)
        if dist[curr] < d:
            continue
        # 도착점에 방문시 종료
        if curr == n + 1:
            return

        for next, nd in graph[curr]:
            if dist[next] > dist[curr] + nd:
                dist[next] = dist[curr] + nd
                heappush(pq, (dist[next], next))


start_x, start_y = map(float, input().split())
end_x, end_y = map(float, input().split())

n = int(input())

arr = []
arr.append((start_x, start_y))
for _ in range(n):
    x, y = map(float, input().split())
    arr.append((x, y))
arr.append((end_x, end_y))

graph = [[] for _ in range(n + 2)]
for i in range(n + 2):
    for j in range(i + 1, n + 2):
        tmp = sqrt((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
        # 시작노드는 달리기만
        if i == 0:
            graph[i].append((j, tmp / 5))
        # 다른 노드들은 달리기와 대포 둘 다
        else:
            graph[i].append((j, tmp / 5))
            graph[i].append((j, 2 + abs(tmp - 50) / 5))
            graph[j].append((i, tmp /5))
            graph[j].append((i, 2 + abs(tmp - 50) / 5))

INF = maxsize
dist = [maxsize] * (n + 2)

dijkstra()
print(dist[n + 1])
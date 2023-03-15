import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
a, b = map(int, input().split())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, b):
    q = deque([a])
    visited = [a]
    counts = 1
    while q:
        # 깊이를 구하기 위해 for문 하나 더 추가
        for _ in range(len(q)):
            curr = q.popleft()
            for adj in graph[curr]:
                if adj not in visited:
                    if adj == b:
                        return counts
                    else:
                        visited.append(adj)
                        q.append(adj)
        counts += 1
    return -1

print(bfs(a, b))
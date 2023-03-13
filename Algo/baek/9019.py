from sys import stdin
from collections import deque
input = stdin.readline


def bfs(a, b, path):
    visited = [False] * 10000
    q = deque([(a, path)])
    while q:
        n, path = q.popleft()
        # 연산 종료
        if n == b:
            return path

        if visited[n]:
            continue
        else:
            visited[n] = True
        # D
        q.append(((n * 2) % 10000, path + 'D'))
        # S
        q.append(((n - 1) % 10000, path + 'S'))
        # L
        q.append((((10 * n + (n // 1000)) % 10000), path + 'L'))
        # R
        q.append(((n // 10 + (n % 10) * 1000) % 10000, path + 'R'))


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b, ''))
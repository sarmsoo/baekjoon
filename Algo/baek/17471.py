from sys import stdin
from collections import deque
input = stdin.readline

def bfs(tmp):
    arr1 = tmp
    arr2 = []
    for i in range(1, n + 1):
        if i not in tmp:
            arr2.append(i)

    q1 = deque([arr1[0]])
    q2 = deque([arr2[0]])
    visited = [0] * (n + 1)
    visited[arr1[0]] = 1
    visited[arr2[0]] = 1
    while q1:
        curr = q1.popleft()
        for next in graph[curr]:
            if visited[next]:
                continue
            if next in arr1:
                visited[next] = 1
                q1.append(next)

    while q2:
        curr = q2.popleft()
        for next in graph[curr]:
            if visited[next]:
                continue
            if next in arr2:
                visited[next] = 1
                q2.append(next)

    # 두 구역으로 잘 나누어졌다면
    if sum(visited) == n:
        sum1 = 0
        for i in arr1:
            sum1 += arr[i]
        sum2 = 0
        for i in arr2:
            sum2 += arr[i]
        return abs(sum1 - sum2)

    return 1e10

def sol(m, depth, start):
    global answer
    if depth == m:
        answer = min(answer, bfs(tmp))
        return

    for i in range(start, n + 1):
        tmp.append(i)

        sol(m, depth + 1, i + 1)

        tmp.pop()


n = int(input())
arr = [0] + list(map(int, input().split()))
graph = [[]]
for i in range(1, n + 1):
    nodes = list(map(int, input().split()))[1:]
    graph.append((nodes))

tmp = []
answer = 1e10
for m in range(1, n // 2 + 1):
    sol(m, 0, 1)

print(answer if answer != 1e10 else -1)
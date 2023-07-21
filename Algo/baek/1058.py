from sys import stdin
input = stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

answer = 0
for i in range(n):
    visited = [False] * n
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] == 'Y':
            visited[j] = True
            for k in range(n):
                if visited[k] or k == i:
                    continue
                if graph[j][k] == 'Y':
                    visited[k] = True

    tmp = sum(visited)
    answer = max(answer, tmp)

print(answer)
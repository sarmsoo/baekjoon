from sys import stdin, maxsize
input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = maxsize

def sol(depth, idx):
    global result
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        result = min(result, abs(power1 - power2))
        return

    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = True
        sol(depth + 1, i + 1)
        visited[i] = False
sol(0, 0)
print(result)
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]


for l in range(min(n, m), 0, -1):
    for i in range(n - l + 1):
        for j in range(m - l + 1):
            if graph[i][j] == graph[i][j + l - 1] == graph[i + l - 1][j] == graph[i + l - 1][j + l - 1]:
                print(l ** 2)
                exit(0)



from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check(line):
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i + j] or visited[i + j]:
                    return False
                if line[i] == line[i + j]:
                    visited[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - 1 - j < 0 or line[i - 1] != line[i - 1 - j] or visited[i - 1 - j]:
                    return False
                if line[i - 1] == line[i - 1 - j]:
                    visited[i - 1 - j] = True
    return True

answer = 0
for i in range(n):
    visited = [False] * n
    if check([graph[i][j] for j in range(n)]):
        answer += 1

for j in range(n):
    visited = [False] * n
    if check([graph[i][j] for i in range(n)]):
        answer += 1

print(answer)
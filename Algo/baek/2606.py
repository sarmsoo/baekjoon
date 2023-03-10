# BFS
'''from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

q = deque([1])
visited[1] = 1
while q:
    curr = q.popleft()
    for next in graph[curr]:
        if visited[next] == 1:
            continue
        q.append(next)
        visited[next] = 1
print(sum(visited) - 1) # 1번 컴퓨터는 더 하면 안됨
'''
# DFS
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

stack = [1]
while stack:
    curr = stack.pop()
    if visited[curr] == 0:
        visited[curr] = 1
        for next in graph[curr]:
            stack.append(next)
print(sum(visited) - 1)





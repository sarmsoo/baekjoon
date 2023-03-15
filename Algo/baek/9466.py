import sys
input = sys.stdin.readline

def dfs(s):
    stack = [s]
    while stack:
        curr_node = stack.pop()
        next_node = graph[curr_node]
        visited[curr_node] = True
        if next_node == s:
            return True
        if not visited[next_node]:
            stack.append(next_node)
    return False
t = int(input())
cycle_node = []
for _ in range(t):
    n = int(input())
    visited = [False] * (n + 1)
    graph = [0] + list(map(int, input().split()))
    for node in range(1, len(graph)):
        if not visited[node]:
            if dfs(node):
                cycle_node = dfs(node)

    print(n - visited.count(True))
    visited = [False] * (n + 1)


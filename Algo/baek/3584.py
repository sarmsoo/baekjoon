from sys import stdin
input = stdin.readline

def dfs(node):
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr == c2:
            return True
        for next in child[curr]:
            stack.append(next)
    return False


for _ in range(int(input())):
    n = int(input())
    parent = [i for i in range(n + 1)]
    child = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a
        child[a].append(b)
    c1, c2 = map(int, input().split())

    curr = c1
    while True:
        if dfs(curr):
            print(curr)
            break
        else:
            curr = parent[curr]
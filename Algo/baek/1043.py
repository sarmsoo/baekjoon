from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
p, *q = list(map(int, input().split()))
checked = [False] * (n + 1)
for i in q:
    checked[i] = True

cnt = 0
check_list = [[] for _ in range(n + 1)]
party = []
check_set = set()

def bfs(i):
    visited = [False] * (m + 1)
    q = deque([i])
    visited[i] = True
    while q:
        curr = q.popleft()
        check_set.add(curr)
        for i in party[curr]:
            for next in check_list[i]:
                if visited[next]:
                    continue
                q.append(next)
                visited[next] = True

for index in range(m):
    a, *b = list(map(int, input().split()))
    party.append(b)
    flag = False
    for people in b:
        if checked[people]:
            flag = True
            break
    if flag:
        for people in b:
            checked[people] = True
            if check_list[people]:
                for i in check_list[people]:
                    bfs(i)
    else:
        cnt += 1
        for people in b:
            check_list[people].append(index)

print(cnt - len(check_set))
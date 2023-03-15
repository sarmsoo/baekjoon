import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
#왜 내꺼는 메모리 초관데 다른 애들은 통관데 코드 같은데 이 ㅆ1발아

n, m, p = map(int, input().split())
graph = [[] for _ in range(m + 1)]
for _ in range(n):
    v, u = map(int, input().split())
    graph[u].append(v)

counts = 0
visited = [False] * (m + 1)
def dfs(s):
    global counts
    visited[s] = True
    if not graph[s]:
        return
    next = graph[s][0]
    if not visited[next]:
        counts += 1
        dfs(next)
    else:
        counts = -1
        return
dfs(p)
print(counts)
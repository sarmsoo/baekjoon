'''
이 문제에서 배운 점이 많이 있다.
1. 맨 처음 이 문제를 접했을 때, 연결된 크기 7의 집합의 모든 경우의 수를 구해야한다고 생각했다.
   그런데 그렇게 하지않고,
   브루트포스로 크기 7의 집합을 모두 구하고 거기에서 인접함을 체크하는 방식으로 푸는 것이다.

2. 이중 for문으로는 재귀구조에서 이전 (i, j)에서 부터 시작하는 것을 구현할려면 코드가 더럽다.
   그래서 그렇게 하지않고 다음과 같이하면 깔끔하다.
   for i in range(start, 25):
       r = i // 5
       c = i % 5

3. sol(depth + 1, i + 1, y + (graph[r][c] == 'Y'))
   위 처럼 짜면 if, else를 하지 않아 코드가 매우 깔끔해진다.
'''
from sys import stdin
from collections import deque
input = stdin.readline

graph = [list(input().strip()) for _ in range(5)]
answer = 0
arr = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(arr):
    visited = [[True] * 5 for _ in range(5)]
    for i in arr:
        visited[i[0]][i[1]] = False
    q = deque([arr[0]])
    visited[arr[0][0]][arr[0][1]] = True
    count = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            q.append((ny, nx))
            count += 1
    if count == 7:
        return True
    else:
        return False

def sol(depth, start, y):
    global answer

    if y >= 4:
        return
    if depth == 7:
        if bfs(arr):
            answer += 1
        return

    for i in range(start, 25): # 2중 for문으로 했을 때, start부터 시작을 구현할려면 어려움.
        r = i // 5
        c = i % 5
        arr.append((r, c))
        sol(depth + 1, i + 1, y + (graph[r][c] == 'Y')) # y + 1을 if문 안쓰고 깔끔하게 이렇게 할 수 있음
        arr.pop()

sol(0, 0, 0)
print(answer)
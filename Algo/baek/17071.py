from sys import stdin
from collections import deque
input = stdin.readline

'''
이전 숨바꼭질 문제들과의 차이점은 동생이 움직인다는 것이다.
동생이 움직이니 이미 방문 했던 곳을 다시 방문할 필요가 있다.
그렇다고 방문을 체크 안한다면 3 ** n 만큼 시간복잡도가 증가해서 시간 제한에 풀어낼 수가 없다.
그래서 방문 체크를 어떻게 해야하는지가 핵심이다.
어떤 좌표에서 2초 뒤에는 반드시 그 좌표로 다시 돌아올 수 있다(x + 1, x- 1).
그러니 홀수, 짝수로 나누어 방문을 체크해주면 된다.

핵심은 동생이 움직이니 방문 체크 방법을 다시 떠올리는 것이다.
'''
def bfs(n, k):
    q = deque([n])
    visited[n][0] = True
    time = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            if k > 500000:
                return -1
            if x == k or visited[k][time % 2]:
                return time

            for nx in [x + 1, x - 1, 2 * x]:
                if nx < 0 or nx > 500000:
                    continue
                if visited[nx][(time + 1) % 2]:
                    continue
                q.append(nx)
                visited[nx][(time + 1) % 2] = True

        time += 1
        k += time

n, k = map(int, input().split())
visited = [[False] * 2 for _ in range(500001)]

print(bfs(n, k))
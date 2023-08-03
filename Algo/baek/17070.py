from sys import stdin
input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n + 1)]

# dp[r][c][dir]
dp = [[[0] * 3 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][1][0] = 1

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            continue
        for dir in range(3):
            if dp[r][c][dir] == 0:
                continue
            # 방향 가로일 때
            if dir == 0:
                dp[r][c + 1][0] += dp[r][c][dir] # 다음 방향 가로
            # 방향 세로일 떄
            elif dir == 1:
                dp[r + 1][c][1] += dp[r][c][dir] # 다음 방향 세로
            # 방향 대각일 때
            else:
                dp[r][c + 1][0] += dp[r][c][dir] # 다음 방향 가로
                dp[r + 1][c][1] += dp[r][c][dir] # 다음 방향 세로

            # 벽 없을 때, 다음 방향 대각
            if graph[r + 1][c] == 1 or graph[r][c + 1] == 1 or graph[r + 1][c + 1] == 1:
               continue
            dp[r + 1][c + 1][2] += dp[r][c][dir]

print(sum(dp[n - 1][n - 1]) if graph[n - 1][n - 1] == 0 else 0)
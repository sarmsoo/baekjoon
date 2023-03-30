from sys import stdin
input = stdin.readline

t, w = map(int, input().split())
arr = [0]
for _ in range(t):
    arr.append(int(input()))
# dp[i번째][1번 나무에 서있는 경우, 2번 나무에 서있는경우][움직일 수 있는 남은 횟수 w]
dp = [[[], [0] * (w + 2), [0] * (w + 2)] for _ in range(t + 1)]

for i in range(1, t + 1):
    for j in range(w + 1):
        # i번째에 1번 나무에서 떨어진다면
        if arr[i] == 1:
            # 1번 나무에 서있을 경우
            dp[i][1][j] = max(dp[i - 1][1][j] + 1, dp[i - 1][2][j + 1] + 1)
            # 2번 나무에 서있을 경우
            dp[i][2][j] = max(dp[i - 1][1][j + 1], dp[i - 1][2][j])

        # i번째에 2번 나무에서 떨어진다면
        elif arr[i] == 2:
            # 처음에 시작할 때 1번 나무에 있음
            # 아............................................
            # 이거 때문에 삽질 한 시간 넘게 했네...........................아
            if i == 1 and j == w:
                continue
            # 1번 나무에 서있을 경우
            dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][2][j + 1])
            # 2번 나무에 서있을 경우
            dp[i][2][j] = max(dp[i - 1][1][j + 1] + 1, dp[i - 1][2][j] + 1)

print(max(max(dp[t][1]), max(dp[t][2])))
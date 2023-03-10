from sys import stdin

input = stdin.readline

# bruteforce
'''
n = int(input())
stairs = [0]
for _ in range(n):
    stair = int(input())
    stairs.append(stair)

def dfs() -> int:
    stack = [(0, 0, 0)]
    answer = 0
    while stack:
        curr = stack.pop()
        x, time, temp = curr
        temp += stairs[x]

        if x == n:
            answer = max(answer, temp)

        if x + 1 <= n and time < 2:
            stack.append((x + 1, time + 1, temp))
        if x + 2 <= n:
            stack.append((x + 2, 1, temp))

    return answer

print(dfs())
'''
# top-down

n = int(input())

stairs = [0]
for _ in range(n):
    stair = int(input())
    stairs.append(stair)

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][1] = stairs[1]
dp[1][0] = 0
if n >= 2:
    dp[2][0] = stairs[2]
    dp[2][1] = stairs[1] + stairs[2]


def sol(x: int, y: int) -> int:
    # 메모이제이션
    if dp[x][y] != 0:
        return dp[x][y]
    if x == 1 or x == 2:
        return dp[x][y]
    # y 가 1이면 이전에서 한 칸 이동, y가 0이면 이전 칸에서 두 칸이동
    if y == 1:
        dp[x][1] = sol(x - 1, 0) + stairs[x]
    if y == 0:
        dp[x][0] = max(sol(x - 2, 1) + stairs[x], sol(x - 2, 0) + stairs[x])
    return dp[x][y]


print(max(sol(n, 0), sol(n, 1)))

# 구글에 top-down 풀이는 별로 없다. 벗, 미? 바로 top-down
# 자랑스럽다 권용진 !
